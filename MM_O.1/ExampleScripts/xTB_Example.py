import random
import sys
sys.path.append("..")
import toolset as mm
from copy import deepcopy as c
import os

#LocalDirectoryToWriteOutput
dir= "../outs"

#Vars
numH2O=10
numCO2=numCO3=1
numModels=100
minR=0
maxR=15

#Load in important XYZs
IRA_900=mm.readXYZ("../xyz/IRA900.xyz")
H2O=mm.readXYZ("../xyz/H2O.xyz")
CO3=mm.readXYZ("../xyz/carbonate.xyz")
CO2=mm.readXYZ("../xyz/CO2.xyz")

#Create Model (nested list of molecules, their atoms, and each atoms position)
model=[IRA_900]
#Name of output folder
name="xTB_Example"
#Directory of output folder
dir=f'{dir}/{name}'

#Check if folder exists and Create Folder if not
if not os.path.exists(dir):
    os.mkdir(dir)
else:
    print("Folder already exists...\nContinuing...")

#Create Manifest File
f = open(dir+"/xTB_run.sh", "w")
f.write("# -------Add Slurm setting here !!--------\nmodule purge\nmodule load xtb\n")

#Create folder name from data
computationalName='xyz'
dir=f'{dir}/{computationalName}'
if not os.path.exists(dir):
    os.mkdir(dir)
else:
    print("folder already exists...\ncontinuing...")

print(model)
#Hydration Folder Format: hydrationLevel_"water"
for ID in range(1,numModels+1):
    cModel = c(model)
    mm.randomPlace(cModel, c(H2O), numH2O, minR, maxR)
    mm.randomPlace(cModel, c(CO2), numCO2, minR, maxR)
    mm.randomPlace(cModel,c(CO3),numCO3,minR,maxR)
    mm.writeXYZ(dir+"/"+str(ID)+".xyz", cModel)
    mm.writeXTB(f,dir,ID)

f.close()

