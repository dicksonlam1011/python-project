import datetime
import os

ppm_sharefolder_path="//dc7shdns02b/CSC1/TEAMFOLDER/PPM"
# month_path=input("Please enter the PPM Month folder (eg: 2021_12): \n")
# ppm_folder=input("Please enter the PPM Folder Name (eg: 2021-S0492(K2)): \n")
month_path="2021_12"
ppm_folder="2021-S0492(K2)"
mypath="{}/{}/{}".format(ppm_sharefolder_path, month_path, ppm_folder)



def checkSybaseSyntax():
    string_to_search_1="GO"
    string_to_search_2="go"

    sql_file_list = []
    for (dirpath, subdirs, files) in os.walk(mypath):
        for x in files:
            if x.endswith((".sql",".ppm",".aat",".pps",".prd")):
                sql_file_list.append(os.path.join(dirpath, x))
            # print(SQLfiles)

    for sql_file in sql_file_list:
        with open(sql_file, 'r') as file:
            file = file.read()
            # print(file)
            if (string_to_search_1 in file) or (string_to_search_2 in file):
                print("{}: Pass".format(sql_file))
            else:
                print("{}: Failed !!!".format(sql_file))



def checkSybaseHeader():
    # File Path List
    sql_file_list = []
    for (dirpath, subdirs, files) in os.walk(mypath):
        for x in files:
            if x.endswith((".sql",".ppm",".aat",".pps",".prd")):
                sql_file_list.append(os.path.join(dirpath, x))

    # File Name List
    sql_filename_list = []
    for (dirpath, subdirs, files) in os.walk(mypath):
        for x in files:
            if x.endswith((".sql",".ppm",".aat",".pps",".prd")):
                sql_filename_list.append(x)


    for sql_file in sql_file_list:
        for header_to_search in sql_filename_list:
            with open(sql_file, 'r') as file:
                file = file.read()
            if header_to_search in file:
                print("{}: Pass".format(header_to_search))
            else:
                print("{}: Failed !!!".format(header_to_search))
        break






        

# for sql_file in sql_file_list:
#     with open(sql_file, 'r') as file:
#         file = file.read()
#         # print(file)
#         if (string_to_search_1 in file) or (string_to_search_2 in file):
#             print("{}: Pass".format(sql_file))
#         else:
#             print("{}: Failed !!!".format(sql_file))








    




