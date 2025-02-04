from copy import deepcopy as c
from random import randint as r
import molecules as molecules
import os
import csv
import numpy as np
import math
from collections import Counter

def calculateDistance(atom1,atom2):
    distance = math.sqrt((atom1[1] - atom2[1]) ** 2 + (atom1[2] - atom2[2]) ** 2 + (atom1[3] - atom2[3]) ** 2)
    return distance

#Used to translate a molecule by (dx,dy,dz)
def translateMolecule(molecule,dx,dy,dz):
    m=c(molecule)
    for atom in range(len(molecule)):
        m[atom][1] += dx
        m[atom][2] += dy
        m[atom][3] += dz
    return m

#Rotate Molecule
def rotateMolecule(molecule,xAngle,yAngle,zAngle):
    #calculate Rotation Matrixes
    Rx=np.matrix([[1, 0, 0],[0, math.cos(-xAngle), -math.sin(-xAngle)],[0, math.sin(-xAngle), math.cos(-xAngle)]])
    Ry=np.matrix([[math.cos(-yAngle), 0, math.sin(-yAngle)],[0, 1, 0],[-math.sin(-yAngle), 0, math.cos(-yAngle)]])
    Rz=np.matrix([[math.cos(-zAngle), -math.sin(-zAngle), 0],[math.sin(-zAngle), math.cos(-zAngle), 0],[0, 0, 1]])
    R=Rx*Ry*Rz

    m = c(molecule)
    for atom in range(len(molecule)):
        newCords=(np.array(m[atom][1:])*R).tolist()[0]
        m[atom][1]=newCords[0]
        m[atom][2] = newCords[1]
        m[atom][3] = newCords[2]
    return m

#Calculate Center of Molecule
def calculateCenter(molecule):
    m = c(molecule)
    x, y, z, atoms = 0, 0, 0, 0
    for atom in range(len(molecule)):

        x += m[atom][1]
        y += m[atom][2]
        z += m[atom][3]
        atoms += 1
    return [x / atoms, y/atoms, z/atoms]

#Centers a molecule around (x,y,z) defaults to (0,0,0)
def centerMolecule(molecule,center=[0,0,0]):
    m = c(molecule)
    oldCenter=calculateCenter(m)
    m=translateMolecule(m,-oldCenter[0]+center[0],-oldCenter[1]+center[1],-oldCenter[2]+center[2])
    return m

def randomPlace(model,molecule,numberMolecules,minRadius,maxRadius,bondDistance=1.8):
    m = c(molecule)
    minRadius=math.sqrt(3*minRadius**2)
    for i in range(numberMolecules):
        greaterThanMinRadius = False
        while greaterThanMinRadius == False:
            randomMolecule=rotateMolecule(translateMolecule(m,r(-maxRadius,maxRadius),r(-maxRadius,maxRadius),r(-maxRadius,maxRadius)),r(0,360),r(0,360),r(0,360))
            minDistance=None
            for molecule in model:
                for atom in molecule:
                    randomCenter=calculateCenter(randomMolecule)
                    distance = math.sqrt( (randomCenter[0]-atom[1])**2 + (randomCenter[1]-atom[2])**2 + (randomCenter[2]-atom[3])**2)
                    if minDistance==None or distance<minDistance:
                        minDistance=distance
            if minDistance>bondDistance:
                greaterThanMinRadius=True
        model.append(randomMolecule)

def pointsAlongLine(startPoint,endPoint,numPoints):
    points=[]
    for p in range(0,numPoints):
        pp=p/numPoints
        point=[startPoint[0]+pp*(endPoint[0]-endPoint[0]),startPoint[1]+pp*(endPoint[1]-endPoint[1]),startPoint[2]+pp*(endPoint[2]-endPoint[2])]
        points.append(point)
    return points
def xlinkPolyPlace(model,molecule,chargeSites,linkSites,startPoint,endPoint):
    m = c(molecule)
    points = pointsAlongLine(startPoint,endPoint,chargeSites+linkSites)

    for i in range(len(points)):
            randomMolecule=translateMolecule(m,points[i][0],points[i][1],points[i][2])
            model.append(randomMolecule)

#Reads an XYZ file and converts to our molecule array format(see molecules script)
def readXYZ(path):
    f = open(path,"r")
    f=f.read().split("\n")
    out=[]
    l=0
    for line in f:
        if l>1 and line!=None and line!="":
            line = line.split(" ")
            lineOut=[]
            for character in line:
                if character!="" and character!=None:
                    try:
                        character=float(character)
                    except:
                        None
                    lineOut.append(character)

            out.append(lineOut)
        l+=1
    out=centerMolecule(out)
    return out

#Used to write an XYZ file from a path and model array
def writeXYZ(path,model):
    f = open(path, "w")
    atoms=0
    string=""
    for molecule in model:
        for atom in molecule:
            atoms+=1
            string+=f'\n{atom[0]} {atom[1]} {atom[2]} {atom[3]}'

    f.write(f'{atoms}\n{string}')
    f.close()

def writeGJF(path,model,settings='%nprocshared=1\n%mem=1GB\n#p opt=(calcfc,cartesian,maxcycles=5000) iop(1/152=5000) pm6\n\nTitle\n\n0 1',params=""):
    f = open(path, "w")
    atoms=0
    string=settings
    for molecule in model:
        for atom in molecule:
            string+=f'\n{atom[0]} {atom[1]} {atom[2]} {atom[3]}'

    f.write(f'{string}\n\n{params}\n')
    f.close()

def writeXTB(file,path,ID,last=999,outName="out24",settings="--opt tight --cycles 3000 --charge 0"):
    if ID != last:
        line="xtb "+path+"/"+str(ID)+".xyz"+" "+settings+"\n"+"rm xtbrestart xtbtopo.mol wbo charges\nmv xtbopt.log out/log/"+str(ID)+".xyz\nmv xtbopt.xyz out/xyz/"+str(ID)+".xyz\n"
    else:
        line = "xtb " + path + "/" + str(ID) + ".xyz" + " " + settings + "\n" + "rm xtbrestart xtbtopo.mol wbo charges\nmv xtbopt.log data/"+outName+"/log/" + str(ID) + ".xyz\nmv xtblast.xyz data/"+outName+"/xyz/" + str(ID) + ".xyz\n"

    file.write(line)

def readXYZText(text):
    f=text.split("\n")
    out=[]
    l=0
    for line in f:
        if l>1 and line!=None and line!="":
            line = line.split(" ")
            lineOut=[]
            for character in line:
                if character!="" and character!=None:
                    try:
                        character=float(character)
                    except:
                        None
                    lineOut.append(character)

            out.append(lineOut)
        l+=1
    out=centerMolecule(out)
    return out

def generateOut(directory):
    """
    Loops through a directory and reads the first line of every file.

    Args:
        directory (str): Path to the directory containing files.

    Returns:
        dict: A dictionary where keys are filenames and values are the first lines of the files.
    """
    outs = {}

    # Check if the directory exists
    directory=directory+'/xyz'
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return outs

    # Loop through all files in the directory
    for filename in os.listdir(directory):
        file_path = f'{directory}/{filename}'
        fileID=filename.split(".")[0]
        # Ensure it's a file (not a directory)
        if os.path.isfile(file_path) and file_path.split(".")[-1]=="xyz":
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    print("----------------")
                    print(file_path)
                    content= file.read()
                    lines=content.split("\n")
                    XYZs = content.split(lines[0]+"\n energy")
                    lastStrucutre=readXYZText(XYZs[-1])
                    molFormulas=analyzeGeometry(lastStrucutre)
                    energy=lines[1].split(" ")[2]

                    #first_line = file.readline().strip()
                    outs[fileID] = {
                        "Energy":energy,
                        "Molecules":molFormulas
                    }
                    print(outs[fileID])
            except Exception as e:
                print(f"Could not read file '{filename}': {e}")
    outs=dict(sorted(outs.items(), key=lambda item: item[1]["Energy"],reverse=True))

    output_file = directory+"/out.csv"

    # Write the dictionary to a CSV file
    with open(output_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(["ID", "Energy"])
        # Write each key-value pair
        for key, value in outs.items():
            writer.writerow([key, value["Energy"],str(value["Molecules"])])
    return outs

params={
    "HC":1.09,
    "CH":1.09,
    "HO":1,
    "OH":1,
    "CC":{
        "-":1.54,
        "--":1.34,
        "---":1.2
    },
    "CO":{
        "-":1.31,
        '--':1.21
    },
    "OC":{
        "-":1.31,
        '--':1.21
    },
    "CN":1.5,
    "NC":1.5,
    "HH":0.74,
    "HN":1.01,
    "NH":1.01,
    "NN":{
        "-":1.45,
        "--":1.25,
        "---":1.10
    },
    "NO":{
        '-':1.4,
        "--":1.21
    },
    "ON":{
        '-':1.4,
        "--":1.21
    },
    "OO":{
        '-':1.48,
        '--':1.21
    }
}
def analyzeGeometry(xyz,bondTolerance=1.05):

    molecules=[]
    for atom_i in xyz:
        for atom_j in xyz[xyz.index(atom_i)+1:]:
            if atom_i!=atom_j:
                bondOrder="-"
                bondType=atom_i[0]+atom_j[0]
                bondDistance = calculateDistance(atom_i,atom_j)
                if isinstance(params[bondType],dict):
                    bondOrder=(min(params[bondType], key=lambda bond: abs(params[bondType][bond] - bondDistance)))
                    bondParam = params[bondType][bondOrder]
                else:
                    bondParam=params[bondType]
                if bondDistance < bondParam*bondTolerance:
                    #print(bondType[0]+bondOrder+bondType[1])
                    if molecules==[]:
                        molecules.append([atom_i,atom_j])
                    else:
                        #Loop through molecules
                        for molecule in molecules:
                            #If atom is in this molecule
                            if atom_i in molecule:
                                #If bonded atom not in this molecule add bond
                                if atom_j not in molecule:
                                    molecule.append(atom_j)
                            #If atom not in molecule but bonded atom is
                            elif atom_j in molecule:
                                for molecule_bad in molecules:
                                    if atom_i in molecule_bad:
                                        for atom in molecule_bad:
                                            if atom not in molecule:
                                                molecule.append(atom)
                                        molecules.remove(molecule_bad)
                                        break
                                pass
                            else:
                                if molecule==molecules[-1]:
                                    for moleculeRedo in molecules:
                                        # If atom is in this molecule
                                        if atom_i in moleculeRedo:
                                            # If bonded atom not in this molecule add bond
                                            if atom_j not in moleculeRedo:
                                                moleculeRedo.append(atom_j)
                                            elif molecule == molecules[-1]:
                                                molecules.append([atom_j])
                                        elif molecule==molecules[-1]:
                                            molecules.append([atom_i])
    formulas =[]
    for molecule in molecules:
        moleculesDict={}
        formula={}
        name = ''
        for atom in molecule:
            if atom[0] not in formula:
                formula[atom[0]]=1
            else:
                formula[atom[0]]=formula[atom[0]]+1

        for key in formula.keys():

            name=name+key+str(formula[key])
        formulas.append(formula)
    formulas=analyzeMolecules(formulas)
    return formulas

def analyzeMolecules(mols):
    newMol=[]
    for mol in mols:
        if mol.get('H', 0) == 2 and mol.get('O', 0) == 1 and len(mol)==2:
            newMol.append("H2O")
        elif mol.get('C', 0) == 1 and mol.get('O', 0) == 3 and len(mol)==2:
            newMol.append("CO3")
        elif mol.get('C', 0) == 26 and mol.get('H', 0) == 41 and mol.get('N', 0) == 2 and len(mol)==3:
            newMol.append("IRA900")
        elif mol.get('H', 0) == 1 and mol.get('C', 0) == 1 and mol.get('O', 0) == 3 and len(mol)==3:
            newMol.append("HCO3")
        elif mol.get('C', 0) == 1 and mol.get('O', 0) == 2 and len(mol)==2:
            newMol.append("CO2")
        elif mol.get('H', 0) == 1 and mol.get('O', 0) == 1 and len(mol)==2:
            newMol.append("OH")
        elif mol.get('H', 0) == 9 and mol.get('C', 0) == 3 and mol.get('N', 0) == 1 and len(mol)==3:
            newMol.append("Trimethylamin")
        elif mol.get("N",0)==1:
            newMol.append("Amine Decomp")
        else:
            newMol.append(f"Unkown Structure: {mol}")
            print(f'Could not find data for molecule{mol}')

    newMol= dict(Counter(newMol))
    return newMol
