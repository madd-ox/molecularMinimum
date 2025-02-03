#File format:
# "IRA900_(#+"WATER")or"DRY"_(FUNCTIONAL GROUP)_(CATION)_(#+"GAP")_minR#_maxR#_notes.gjf"

name="IRA900_3WATER_ETHYL_NITROGEN_1GAP_minR5_maxR10_No Notes.gjf"

def readGaussianOut(path):
    f=open(path,"r")
    f=f.read().split("\n")
    for line in reversed(f):
        if "failed for dihedral" in line:
            print("dihedral error")
        if "Error" in line:
            print(line)
            if "9999" in line:
                print("Did not converge")
        elif "E(" in line:
            line=line.split(" ")
            print(line[7])
            break

readGaussianOut("10waterPM7.log")



#p1='%nprocshared=1\n%mem=1GB\n#p opt=(calcfc,cartesian,maxcycles=5000) iop(1/152=5000) pm6\n\nTitle\n\n0 1'
