import datetime
import os

ppm_sharefolder_path="//dc7shdns02b/CSC1/TEAMFOLDER/PPM"
month_path=input="2021_12"
ppm_number="2021-S0492(K2)"
mypath="{}/{}/{}".format(ppm_sharefolder_path, month_path, ppm_number)

# print(os.listdir(mypath))

#  OS.walk() generates file names in a directory tree.  
# for (root, dirs, file) in os.walk(mypath):
#     for f in file:
#         if ".sql" in f:
#             print(f)

SQLfiles = []
for (dirpath, subdirs, files) in os.walk(mypath):
    for x in files:
        if x.endswith(".sql"):
            SQLfiles.append(os.path.join(dirpath, x))
        print(SQLfiles)


# print(os.listdir(mypath))

#  OS.walk() generates file names in a directory tree.  
# for (root, dirs, file) in os.walk(mypath):
#     for f in file:
#         if ".sql" in f:
#             print(f)








    




