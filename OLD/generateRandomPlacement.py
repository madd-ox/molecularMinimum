import random

import toolset as mm
from copy import deepcopy as c
import os

dir= "folders"

minWaters=24
maxWaters=24
minR=1
maxR=10
modelPerHydration=1000

#Model folder format: BaseModel_FunctionalGroup_Cation_Spacing
#Load in model and name
modelPath="models/1water.xyz"
model=[mm.readXYZ("models/IRA900_Carbonate.xyz")]
modelName="24WaterIRA900Test_1000"

dir=f'{dir}/{modelName}'

#Create Model Folder and data CSV
if not os.path.exists(dir):
    os.mkdir(dir)
else:
    print("Folder already exists...\nContinuing...")

#Create Manifest File
f = open(dir+"/manifest.txt", "w")


#Computational folder format: Method_CalculationType_params_proccesors_mem
#Create folder name from data
computationalName='xyz'
dir=f'{dir}/{computationalName}'
if not os.path.exists(dir):
    os.mkdir(dir)
else:
    print("folder already exists...\ncontinuing...")

H2O=mm.readXYZ("models/H2O.xyz")
CO3=mm.readXYZ("models/carbonate.xyz")
CO2=mm.readXYZ("models/CO2.xyz")

#Center waters around nitrocenter
nitrogens=[]
for atom in model[0]:
    if atom[0]=="N":
        nitrogens.append(atom)
nitroCenter=mm.calculateCenter(nitrogens)

nitroCenterH2O=mm.translateMolecule(H2O,nitroCenter[0],nitroCenter[1],nitroCenter[2])
nitroCenterCO2=mm.translateMolecule(CO2,nitroCenter[0],nitroCenter[1],nitroCenter[2])

#Hydration Folder Format: hydrationLevel_"water"
for hydrationLevel in range(minWaters,maxWaters+1):
    hydrationName=str(hydrationLevel)+"water_minR"+str(minR)+"_maxR"+str(maxR)
    hDir = f'{dir}/{hydrationName}'
    if not os.path.exists(hDir):
        os.mkdir(hDir)
    else:
        print("ERROR: HYDRATION FOLDER ALREADY EXISTS")
        exit(1)

    for ID in range(modelPerHydration):
        cModel = c(model)
        mm.randomPlace(cModel, c(nitroCenterH2O), hydrationLevel, minR, maxR)
        mm.randomPlace(cModel, c(nitroCenterCO2), 1, minR, maxR)
        mm.writeXYZ(hDir+"/"+str(ID)+".xyz", cModel)
        mm.writeXTB(f,hDir,ID)
    hydrationLevel = hydrationLevel + 1

f.close()
#Add Random Waters to model
#
#p1='%nprocshared=1\n%mem=1GB\n#p opt=(calcfc,cartesian,maxcycles=5000) iop(1/152=5000) pm6\n\nTitle\n\n0 1'

#Place Molecules

