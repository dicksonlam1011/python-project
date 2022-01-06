import datetime
import os
import operator

def getAllSqlFileList(mypath):
    sql_file_list = []
    for (dirpath, subdirs, files) in os.walk(mypath):
        for x in files:
            if x.endswith((".sql",".ppm",".aat",".pps",".prd")):
                sql_file_list.append(os.path.join(dirpath, x))
    return sql_file_list


def getSpecificTypeSqlFilelist(script_type, mypath):
    sql_file_list = []
    for (dirpath, subdirs, files) in os.walk(mypath):
        for x in files:
            # if operator.contains(x, "imp-corp-db"):
            if x.endswith((".sql",".ppm",".aat",".pps",".prd")) and (script_type in dirpath):
                sql_file_list.append(os.path.join(dirpath, x))
    return sql_file_list

def getFileNameOnly(sql_file_list):
    # get filename only
    filename=[]
    for sql_file in sql_file_list:
        filename.append(sql_file.split("\\")[-1])
    return filename

# get the last 4 element in the file path list
def getFileName(sql_file_list):
    temp_list=[]
    file_path=[]
    for sql_file in sql_file_list:
        file_path.append('/'.join(map(str, sql_file.split("\\")[-4:])))
    return file_path

# Function 1: check header
def checkHeaderInTheScript(content, mypath):
    filename_list=getFileNameOnly(getAllSqlFileList(mypath))
    for filename in filename_list:
        if filename in content:
            return filename

def checkSybaseHeader(sql_file_list, mypath):
    HeaderMatchedList=[]
    for sql_file in sql_file_list:
        with open(sql_file, 'r', encoding="utf-8") as file:
            file = file.read()
            HeaderMatchedList.append(checkHeaderInTheScript(file, mypath))

    filename_list=getFileNameOnly(getAllSqlFileList(mypath))
    # print(filename_list)
    # print(HeaderMatchedList)
    return set(filename_list).difference(HeaderMatchedList)


# Function 2: check basic syntax
def checkSybaseBasicSyntax(sql_file_list, string_to_search):
    checkBasicSyntaxResult=[]
    # print(sql_file_list)
    for sql_file in sql_file_list:
        with open(sql_file, 'r', encoding="utf-8") as file:
            file = file.read()
            if (string_to_search.lower() not in file) and (string_to_search.upper() not in file) and (string_to_search not in file):
                checkBasicSyntaxResult.append(sql_file)
    return getFileName(checkBasicSyntaxResult)

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
    checkHospcodeResult=getFileName(checkHospcodeResult)
    return checkHospcodeResult

# Function 5: check script special issue
def checkScriptSpecialIssues(sql_file_list, string_to_search):
    check_script_result=[]
    for sql_file in sql_file_list:
        with open(sql_file, 'r', encoding="utf-8") as file:
            file = file.read()
            if (string_to_search.lower() in file) or (string_to_search.upper() in file):
                check_script_result.append(sql_file)
    return getFileName(check_script_result)

# print(checkScriptSpecialIssues(getAllSqlFileList(),"menu_function_list"))

# Function 6: check manual cicd unsupported scripts
def checkUnsupportedScript(sql_file_list, string_to_search):
    filtered_list=[]
    for sql_file in sql_file_list:
        with open(sql_file, 'r', encoding="utf-8") as file:
            file = file.read()
            if ((string_to_search.lower() in file) or (string_to_search.upper() in file)) and ("_imp-manual_" not in sql_file) and ("_manual_" not in sql_file):
                filtered_list.append(sql_file)
    filtered_list=getFileName(filtered_list)
    # filename_list=getFileNameOnly(getAllSqlFileList())
    # print(filename_list)
    # print(HeaderMatchedList)
    return filtered_list

# Function 7: check file path
def checkFilePath(sql_file_list, string_to_search_1, string_to_search_2):
    filtered_list=[]
    # print(sql_file_list)
    for sql_file in sql_file_list:
        if (string_to_search_1 in sql_file) and (string_to_search_2 in sql_file):
            filtered_list.append(sql_file)
    return getFileName(filtered_list)


# sql_file="//dc7shdns02b/CSC1/TEAMFOLDER/PPM/2021_12/Dickson_test/DP_010_imp-corp-db_UpdateCorpForwarder/DB_SERVER_LIST_CORP/corp/010_psycis29_upd_corp_forwarder.sql"
# file = open(sql_file, 'r', encoding="utf-8")
# lines = list(file.readlines())
# for line in lines:
#     i=len(lines)
#     lastline=lines[len(lines)-i]
#     print(lastline)
    # lastline=lines[len(lines)-1]
    # print(lastline)




        








    



