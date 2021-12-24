import datetime
import os
import operator

ppm_sharefolder_path="//dc7shdns02b/CSC1/TEAMFOLDER/PPM"
# month_path=input("Please enter the PPM Month folder (eg: 2021_12): \n")
# ppm_folder=input("Please enter the PPM Folder Name (eg: 2021-S0492(K2)): \n")
month_path="2021_12"
ppm_folder="2021-U0313(K2)"
mypath="{}/{}/{}".format(ppm_sharefolder_path, month_path, ppm_folder)

def getAllSqlFileList():
    sql_file_list = []
    for (dirpath, subdirs, files) in os.walk(mypath):
        for x in files:
            if x.endswith((".sql",".ppm",".aat",".pps",".prd")):
                sql_file_list.append(os.path.join(dirpath, x))
    return sql_file_list

def getAllSqlNameList():
    sql_filename_list = []
    for (dirpath, subdirs, files) in os.walk(mypath):
        for x in files:
            if x.endswith((".sql",".ppm",".aat",".pps",".prd")):
                sql_filename_list.append(x)
    return sql_filename_list

def getSpecificTypeSqlFilelist(script_type):
    sql_file_list = []
    for (dirpath, subdirs, files) in os.walk(mypath):
        for x in files:
            # if operator.contains(x, "imp-corp-db"):
            if x.endswith((".sql",".ppm",".aat",".pps",".prd")) and (script_type in dirpath):
                sql_file_list.append(os.path.join(dirpath, x))
    return sql_file_list

def getSpecificTypeSqlNameList(script_type):
    sql_filename_list = []
    for (dirpath, subdirs, files) in os.walk(mypath):
        for x in files:
            if x.endswith((".sql",".ppm",".aat",".pps",".prd")) and (script_type in dirpath):
                sql_filename_list.append(x)
    return sql_filename_list

# Function 1: check header
def checkSybaseHeader(sql_file_list, sql_filename_list):
    checkHeaderResult=[]
    for sql_file in sql_file_list:
        for header_to_search in sql_filename_list:
            with open(sql_file, 'r', encoding="utf-8") as file:
                file = file.read()
            if header_to_search in file:
                checkHeaderResult.append("{}: Header Pass".format(header_to_search))
            else:
                checkHeaderResult.append("{}: Header Failed !!!".format(header_to_search))
        break
    return checkHeaderResult


# Function 2: check basic syntax
def checkSybaseBasicSyntax(sql_file_list, sql_filename_list, string_to_search_1, string_to_search_2):
    checkBasicSyntaxResult=[]
    for sql_file in sql_file_list:
        for sql_filename in sql_filename_list:
            with open(sql_file, 'r', encoding="utf-8") as file:
                file = file.read()
                if (string_to_search_1 in file) or (string_to_search_2 in file):
                    checkBasicSyntaxResult.append("{}: Basic Syntax Pass".format(sql_filename))
                else:
                    checkBasicSyntaxResult.append("{}: Basic Syntax Failed !!!".format(sql_filename))
        break
    return checkBasicSyntaxResult

# Function 3: check db and table match
# def checkSybaseDBandTable(sql_file_list, use_db, table):
#     for sql_file in sql_file_list:
#         with open(sql_file, 'r', encoding="utf-8") as file:
#             file = file.read()
#             if (use_db in file) and (table in file):
#                 print("{}: DB & Table Structure Pass".format(sql_file))
#             else:
#                 print("{}: DB & Table Structure Failed !!!".format(sql_file))

# Function 4: check hospcode
def checkSybaseHospcode(manual_sql_file_list, manual_sql_filename_list, hospcode):
    checkHospcodeResult=[]
    for sql_file in manual_sql_file_list:
        for manual_sql_filename in manual_sql_filename_list:
            with open(sql_file, 'r', encoding="utf-8") as file:
                file = file.read()
                # if (script_type in sql_file) and (hospcode in file):
                if hospcode in file:
                    checkHospcodeResult.append("{}: Hospcode Match Pass".format(manual_sql_filename))
                else:
                    checkHospcodeResult.append("{}: Hospcode Match Failed !!!".format(manual_sql_filename))
        break
    return checkHospcodeResult

def OutputResult():
    header_result=checkSybaseHeader(getAllSqlFileList(), getAllSqlNameList())
    basic_syntax_result=checkSybaseBasicSyntax(getAllSqlFileList(), getAllSqlNameList(), "go", "GO")
    corp_hospcode_result=checkSybaseHospcode(getSpecificTypeSqlFilelist("_manual_"), getSpecificTypeSqlNameList("_manual_"),"HAH")
    hosp_hospcode_result=checkSybaseHospcode(getSpecificTypeSqlFilelist("_imp-manual_"), getSpecificTypeSqlNameList("_imp-manual_"), "hospcode")

    with open(os.path.join(mypath,"{}-header-checking_result.log".format(ppm_folder)), mode="w",encoding="utf8") as file:
        for result in header_result:
            file.write(result+"\n")

    with open(os.path.join(mypath,"{}-syntax-checking_result.log".format(ppm_folder)), mode="w",encoding="utf8") as file:
        for result in basic_syntax_result:
            file.write(result+"\n") 
    
    with open(os.path.join(mypath,"{}-corp-hospcode-checking_result.log".format(ppm_folder)), mode="w",encoding="utf8") as file:
        for result in corp_hospcode_result:
            file.write(result+"\n") 
    
    with open(os.path.join(mypath,"{}-hosp-hospcode-checking_result.log".format(ppm_folder)), mode="w",encoding="utf8") as file:
        for result in hosp_hospcode_result:
            file.write(result+"\n") 
    


    # file = open(os.path.join(mypath,"{}-checking_result.log".format(ppm_folder)), mode="w",encoding="utf8")
    # header_result=checkSybaseHeader(getAllSqlFileList(), getAllSqlNameList())
    # basic_syntax_result=checkSybaseBasicSyntax(getAllSqlFileList(), getAllSqlNameList(), "go", "GO")
    # corp_hospcode_result=checkSybaseHospcode(getSpecificTypeSqlFilelist("_manual_"), getSpecificTypeSqlNameList("_manual_"),"HAH")
    # hosp_hospcode_result=checkSybaseHospcode(getSpecificTypeSqlFilelist("_imp-manual_"), getSpecificTypeSqlNameList("_imp-manual_"), "hospcode")

    # for result in header_result:
    #     file.write(result+"\n")

    # for result in basic_syntax_result:
    #     file.write(result+"\n")

    # for result in corp_hospcode_result:
    #     file.write(result+"\n")

    # for result in hosp_hospcode_result:
    #     file.write(result+"\n")

    # file.close()

OutputResult()
        

# def runCodeScanner():
# print(checkSybaseHeader(getAllSqlFileList(), getAllSqlNameList()))
# print(checkSybaseBasicSyntax(getAllSqlFileList(), "go", "GO"))
# print(checkSybaseHospcode(getSpecificTypeSqlFilelist("_manual_"),"HAH"))
# print(checkSybaseHospcode(getSpecificTypeSqlFilelist("_manual_"),"hospcode"))


# runCodeScanner()







        








    




