import toolset as mm
from copy import deepcopy as c
import os
import shutil

#Define Directory
dir= "OLD/folders/1water"

#Define Settings and Parameters
settings='%nprocshared=1\n%mem=1GB\n#DFTBA opt=(calcfc,cartesian,maxcycles=5000) iop(1/152=5000)\n\nTitle\n\n-2 1'
DFTBAsettings='%nprocshared=1\n%mem=1GB\n#DFTBA opt=(calcfc,cartesian,maxcycles=5000) iop(1/152=5000)\n\nTitle\n\n-2 1'
AMBERsettings='%nprocshared=1\n%mem=1GB\n# amber opt=(calcfc)\n\nTitle\n\n-2 1'
settings=AMBERsettings

params=''
computationalName='AmberTest'

#Model folder format: BaseModel_FunctionalGroup_Cation_Spacing
#Load in model and name
path= "models/IRA900_METHYL_NITROGEN_1space.xyz"
modelName=path.split("/")[-1].split(".xyz")[0]
model=[mm.readXYZ(path)]

#Create Manifest File
f = open(dir+"/manifest4.txt", "a")

#Computational folder format: Method_CalculationType_params_proccesors_mem
#Create folder name from data

path=f'{dir}/{computationalName}'
if os.path.exists(path):
    print("ERROR: FOLDER ALREADY EXISTS")
    exit(1)
else:
    os.mkdir(path)

for hydrationFolder in os.listdir(f'{dir}/xyz/'):
    path=f'{dir}/xyz/{hydrationFolder}'
    print(path)
    os.mkdir(f'{dir}/{computationalName}/{hydrationFolder}')
    for model in os.listdir(path):
        name=model.split(".")[0]
        model=mm.readXYZ(path+'/'+model)
        mm.writeGJF(f'{dir}/{computationalName}/{hydrationFolder}/{name}.gjf', [model], settings=settings, params=params)
        f.write(computationalName+"/"+hydrationFolder+'/'+name+".gjf"+"\n")