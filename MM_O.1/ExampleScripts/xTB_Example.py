import random
import sys
sys.path.append("..")
import toolset as mm
from copy import deepcopy as c
import os

#LocalDirectoryToWriteOutput

dir= "../outs"
#Vars
numH2O=40
numCO2=numCO3=1
numModels=1000
minR=0
maxR=16

#Load in important XYZs
IRA_900=mm.readXYZ("../xyz/IRA900.xyz")
H2O=mm.readXYZ("../xyz/H2O.xyz")
CO3=mm.readXYZ("../xyz/carbonate.xyz")
CO2=mm.readXYZ("../xyz/CO2.xyz")

#Create Model (nested list of molecules, their atoms, and each atoms position)
model=[IRA_900]
#Name of output folder
name="40Water"
#Directory of output folder
dir=f'{dir}/{name}'

#Check if folder exists and Create Folder if not
if not os.path.exists(dir):
    os.mkdir(dir)
else:
    print("Folder already exists...\nContinuing...")

#Create Manifest File
f = open(dir+"/run.sh", "w")

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
    mm.randomPlace(cModel, c(CO3), numCO3, 0, 3)
    mm.randomPlace(cModel, c(H2O), 20, minR, maxR / 2)
    mm.randomPlace(cModel, c(CO2), numCO2, maxR/2, maxR)
    mm.randomPlace(cModel, c(H2O), 20, minR, maxR)


    mm.writeXYZ(dir+"/"+str(ID)+".xyz", cModel)
    mm.writeXTB(f,dir,ID)
    print(str(round(int(ID)/(numModels+1)*100,2))+"%")
f.close()

