from copy import deepcopy as c
from random import randint as r
import molecules as molecules
import numpy as np
import math

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