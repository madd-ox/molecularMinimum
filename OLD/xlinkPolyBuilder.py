import toolset as mm
from copy import deepcopy as c
import os

dir= "folders"

chargeSites=7
crossLinkers=0

#Model folder format: BaseModel_FunctionalGroup_Cation_Spacing
#Load in model and name
chargeSitePath="models/chargeSite.xyz"
#model=[mm.readXYZ("models/poly.xyz")]
model=[]
modelName="poly"
numModels=10

dir=f'{dir}/{modelName}'

#Create Model Folder and data CSV
if not os.path.exists(dir):
    os.mkdir(dir)
else:
    print("Folder already exists...\nContinuing...")

#Computational folder format: Method_CalculationType_params_proccesors_mem
#Create folder name from data
computationalName='xyz'
dir=f'{dir}/{computationalName}'
if not os.path.exists(dir):
    os.mkdir(dir)
else:
    print("folder already exists...\ncontinuing...")

chargeSite=mm.readXYZ(chargeSitePath)

#Center waters around nitrocenter
#nitrogens=[]
#for atom in model[0]:
#    if atom[0]=="N":
#        nitrogens.append(atom)
#nitroCenter=mm.calculateCenter(nitrogens)

#nitroCenterH2O=mm.translateMolecule(H2O,nitroCenter[0],nitroCenter[1],nitroCenter[2])

#Hydration Folder Format: hydrationLevel_"water"

cName=str(chargeSites)+"poly"
hDir = f'{dir}/{cName}'
if not os.path.exists(hDir):
    os.mkdir(hDir)
else:
    print("FOLDER ALREADY EXISTS")


for ID in range(numModels):
    cModel = c(model)
    mm.xlinkPolyPlace(cModel, chargeSite, 7, 0, [0,0,0], [14,14,14])
    mm.writeXYZ(hDir+"/"+str(ID)+".xyz", cModel)


#Add Random Waters to model
#
#p1='%nprocshared=1\n%mem=1GB\n#p opt=(calcfc,cartesian,maxcycles=5000) iop(1/152=5000) pm6\n\nTitle\n\n0 1'

#Place Molecules

