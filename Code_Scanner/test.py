import datetime
import os
import operator

ppm_sharefolder_path="//dc7shdns02b/CSC1/TEAMFOLDER/PPM"
# month_path=input("Please enter the PPM Month folder (eg: 2021_12): \n")
# ppm_folder=input("Please enter the PPM Folder Name (eg: 2021-S0492(K2)): \n")
month_path="2021_12"
# ppm_folder="Dickson_test"
ppm_folder="2021-U0313(K2)"
mypath="{}/{}/{}".format(ppm_sharefolder_path, month_path, ppm_folder)

def getAllSqlFileList():
    sql_file_list = []
    for (dirpath, subdirs, files) in os.walk(mypath):
        for x in files:
            if x.endswith((".sql",".ppm",".aat",".pps",".prd")):
                sql_file_list.append(os.path.join(dirpath, x))
    return sql_file_list


# def getAllSqlNameList():
#     sql_filename_list = []
#     for (dirpath, subdirs, files) in os.walk(mypath):
#         for x in files:
#             if x.endswith((".sql",".ppm",".aat",".pps",".prd")):
#                 sql_filename_list.append(x)
#     return sql_filename_list

def getSpecificTypeSqlFilelist(script_type):
    sql_file_list = []
    for (dirpath, subdirs, files) in os.walk(mypath):
        for x in files:
            # if operator.contains(x, "imp-corp-db"):
            if x.endswith((".sql",".ppm",".aat",".pps",".prd")) and (script_type in dirpath):
                sql_file_list.append(os.path.join(dirpath, x))
    return sql_file_list

# def getSpecificTypeSqlNameList(script_type):
#     sql_filename_list = []
#     for (dirpath, subdirs, files) in os.walk(mypath):
#         for x in files:
#             if x.endswith((".sql",".ppm",".aat",".pps",".prd")) and (script_type in dirpath):
#                 sql_filename_list.append(x)
#     return sql_filename_list

def getFileNameOnly(sql_file_list):
    # get filename only
    filename=[]
    for sql_file in sql_file_list:
        filename.append(sql_file.split("\\")[-1])
    return filename

# Function 1: check header
def checkHeaderInTheScript(content):
    filename_list=getFileNameOnly(getAllSqlFileList())
    for filename in filename_list:
        if filename in content:
            return filename

def checkSybaseHeader(sql_file_list):
    HeaderMatchedList=[]
    for sql_file in sql_file_list:
        with open(sql_file, 'r', encoding="utf-8") as file:
            file = file.read()
            HeaderMatchedList.append(checkHeaderInTheScript(file))

    filename_list=getFileNameOnly(getAllSqlFileList())
    # print(filename_list)
    # print(HeaderMatchedList)
    return set(filename_list).difference(HeaderMatchedList)

# Function 2: check basic syntax
def checkSybaseBasicSyntax(sql_file_list, string_to_search):
    checkBasicSyntaxResult=[]
    for sql_file in sql_file_list:
        with open(sql_file, 'r', encoding="utf-8") as file:
            file = file.read()
            if (string_to_search.lower() not in file) and (string_to_search.upper() not in file):
                checkBasicSyntaxResult.append(sql_file)
    return getFileNameOnly(checkBasicSyntaxResult)

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
def checkSybaseHospcode(sql_file_list, hospcode):
    checkHospcodeResult=[]
    for sql_file in sql_file_list:
        # for sql_filename in sql_filename_list:
        with open(sql_file, 'r', encoding="utf-8") as file:
            file = file.read()
            # if (script_type in sql_file) and (hospcode in file):
            if hospcode in file:
                checkHospcodeResult.append(sql_file)

    return getFileNameOnly(checkHospcodeResult)

def OutputResult():
    # check header match
    # header_result=checkSybaseHeader(getAllSqlFileList(), getAllSqlNameList())
    # # check syntax "go"
    # basic_syntax_result=checkSybaseBasicSyntax(getAllSqlFileList(), getAllSqlNameList(), "go")
    # # check script type (fail case)
    # corp_hospcode_result=checkSybaseHospcode(getSpecificTypeSqlFilelist("_corp-db_"), getSpecificTypeSqlNameList("_corp-db_"), "##hospcode##")
    # hosp_hospcode_result=checkSybaseHospcode(getSpecificTypeSqlFilelist("_imp-corp-db_"), getSpecificTypeSqlNameList("_imp-corp-db_"), "HAH")

    # with open(os.path.join(mypath,"{}-header-checking_result.log".format(ppm_folder)), mode="w",encoding="utf8") as file:
    #     for result in header_result:
    #         file.write(result+"\n")

    # with open(os.path.join(mypath,"{}-syntax-checking_result.log".format(ppm_folder)), mode="w",encoding="utf8") as file:
    #     for result in basic_syntax_result:
    #         file.write(result+"\n") 
    
    # with open(os.path.join(mypath,"{}-corp-hospcode-checking_result.log".format(ppm_folder)), mode="w",encoding="utf8") as file:
    #     for result in corp_hospcode_result:
    #         file.write(result+"\n") 
    
    # with open(os.path.join(mypath,"{}-hosp-hospcode-checking_result.log".format(ppm_folder)), mode="w",encoding="utf8") as file:
    #     for result in hosp_hospcode_result:
    #         file.write(result+"\n") 
    

    file = open(os.path.join(mypath,"{}-checking_result.log".format(ppm_folder)), mode="w",encoding="utf8")
    header_result=checkSybaseHeader(getAllSqlFileList())
    basic_syntax_result=checkSybaseBasicSyntax(getAllSqlFileList(),"go")
    corp_hospcode_result=checkSybaseHospcode(getSpecificTypeSqlFilelist("_corp-db_"),"##hospcode##")
    hosp_hospcode_result=checkSybaseHospcode(getSpecificTypeSqlFilelist("_imp-corp-db_"),"HAH" )

    file.write("=================Header Scanning Result====================="+"\n")
    for result in header_result:
        file.write(result+": Header Result Failed!! "+"\n")

    file.write("=================Syntax Scanning Result====================="+"\n")
    for result in basic_syntax_result:
        file.write(result+": Go is missing in the script !! "+"\n")

    file.write("=================Central script variable Scanning Result====================="+"\n") 
    for result in corp_hospcode_result:
        file.write(result+": Central script variable mistake!! "+"\n")

    file.write("=================Hospital script variable Scanning Result====================="+"\n") 
    for result in hosp_hospcode_result:
        file.write(result+": Hospital script variable mistake!! "+"\n")

    file.close()

OutputResult()
        

# def runCodeScanner():
# print(checkSybaseHeader(getAllSqlFileList(), getAllSqlNameList()))
# print(checkSybaseBasicSyntax(getAllSqlFileList(), "go", "GO"))
# print(checkSybaseHospcode(getSpecificTypeSqlFilelist("_manual_"),"HAH"))
# print(checkSybaseHospcode(getSpecificTypeSqlFilelist("_manual_"),"hospcode"))


# runCodeScanner()







        








    




