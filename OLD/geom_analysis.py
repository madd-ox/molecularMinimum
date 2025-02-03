import toolset as mm

#RDkit 2023.09.1

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
                bondDistance = mm.calculateDistance(atom_i,atom_j)
                if isinstance(params[bondType],dict):
                    bondOrder=(min(params[bondType], key=lambda bond: abs(params[bondType][bond] - bondDistance)))
                    bondParam = params[bondType][bondOrder]
                else:
                    bondParam=params[bondType]
                if bondDistance < bondParam*bondTolerance:
                    print(bondType[0]+bondOrder+bondType[1])
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
        print(name)
        print(formula)



analyzeGeometry(mm.readXYZ("folders/8WaterMMIRA900Test/xyz/8water_minR1_maxR10/0.xyz"), bondTolerance=1.05)