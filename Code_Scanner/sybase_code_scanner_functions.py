import datetime
import os
import operator
import re


def getAllFileList(mypath):
    all_file_list = []
    for (dirpath, subdirs, files) in os.walk(mypath):
        for x in files:
            all_file_list.append(os.path.join(dirpath, x))
    return all_file_list


def getAllSqlFileList(mypath):
    sql_file_list = []
    for (dirpath, subdirs, files) in os.walk(mypath):
        for x in files:
            if x.endswith((".sql".upper(),".sql".lower(),".ppm",".aat",".pps",".prd")):
                sql_file_list.append(os.path.join(dirpath, x))
    return sql_file_list

def getAllSpecialSqlFileList(mypath):
    sql_file_list = []
    for (dirpath, subdirs, files) in os.walk(mypath):
        for x in files:
            if not x.endswith((".sql",".ppm",".aat",".pps",".prd")):
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

def getSpecificTypeCheckingSqlFilelist(script_type, special_checking  , mypath):
    sql_file_list = []
    for (dirpath, subdirs, files) in os.walk(mypath):
        for x in files:
            # if operator.contains(x, "imp-corp-db"):
            if x.endswith((".sql",".ppm",".aat",".pps",".prd")) and (script_type in dirpath) and (special_checking in dirpath) :
                sql_file_list.append(os.path.join(dirpath, x))
    return sql_file_list

def getFileNameOnly(sql_file_list):
    # get filename only
    filename=[]
    for sql_file in sql_file_list:
        filename.append(sql_file.split("\\")[-1])
    return filename

# def getFileNameOnlyWithoutSeqNumnber(filename):
#     # get filename only
#     filename=[]
#     filename_without_seq_mumber=[]
#     for sql_file in sql_file_list:
#         filename.append(sql_file.split("\\")[-1][4:])
#     return filename

# print(getFileNameOnlyWithoutSeqNumnber("040_CCE-164_script_insert_team_call_rules_rollback.sql"))

# get the last 4 element in the file path list
def getFileName(sql_file_list):
    temp_list=[]
    file_path=[]
    for sql_file in sql_file_list:
        file_path.append('/'.join(map(str, sql_file.split("\\")[-4:])))
    return file_path

# Function 1: check header
# def checkHeaderInTheScript(content, mypath):
#     filename_list=getFileNameOnly(getAllSqlFileList(mypath))
#     for filename in filename_list:
#         if filename[4:] in content:
#             return filename

def checkSybaseHeader(sql_file_list, mypath):
    HeaderMatchedList=[]
    for sql_file in sql_file_list:
        with open(sql_file, 'r', encoding="utf-8", errors='ignore') as file:
            file = file.read()
            # print(sql_file.split("\\")[-1][4:])
            # if sql_file.split("\\")[-1][4:] in file:
            if sql_file.split("\\")[-1] in file:
                HeaderMatchedList.append(sql_file.split("\\")[-1])

    filename_list=getFileNameOnly(getAllSqlFileList(mypath))
    # print(filename_list)
    # print(HeaderMatchedList)
    return set(filename_list).difference(HeaderMatchedList)


# Function 2: check basic syntax
def checkSybaseBasicSyntax(sql_file_list, string_to_search):
    checkBasicSyntaxResult=[]
    # print(sql_file_list)
    for sql_file in sql_file_list:
        with open(sql_file, 'r', encoding="utf-8", errors='ignore') as file:
            file = file.read()
            if (string_to_search.lower() not in file) and (string_to_search.upper() not in file) and (string_to_search not in file):
                checkBasicSyntaxResult.append(sql_file)
    return getFileName(checkBasicSyntaxResult)


# Function 3: check db and table match
# def checkSybaseDBandTable(sql_file_list, use_db, table):
#     for sql_file in sql_file_list:
#         with open(sql_file, 'r', encoding="utf-8", errors='ignore') as file:
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
        with open(sql_file, 'r', encoding="utf-8", errors='ignore') as file:
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
        with open(sql_file, 'r', encoding="utf-8", errors='ignore') as file:
            file = file.read()
            if (string_to_search.lower() in file) or (string_to_search.upper() in file) or (string_to_search in file):
                check_script_result.append(sql_file)
    return getFileName(check_script_result)

# print(checkScriptSpecialIssues(getAllSqlFileList(),"menu_function_list"))

# Function 6: check manual cicd unsupported scripts
def checkUnsupportedScript(sql_file_list, string_to_search):
    filtered_list=[]
    for sql_file in sql_file_list:
        with open(sql_file, 'r', encoding="utf-8", errors='ignore') as file:
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


# Function 8: check GO in the last line
def checkLastLine(sql_file_list, string_to_search):
    filtered_list=[]
    for sql_file in sql_file_list:
        with open(sql_file, 'r', encoding="utf-8", errors='ignore') as file:
            lines = (line.rstrip() for line in file)
            lines = list(line for line in lines if line) 
            if len(lines) > 0:
                lastline=lines[len(lines)-1]
                if (lastline!=string_to_search.lower()) and (lastline!=string_to_search.upper()) and (lastline!=string_to_search):
                    filtered_list.append(sql_file)
            # print(lastline)
            # filtered_list.append(lastline)
    return getFileName(filtered_list)

# Function 9: get the file path last element
def getfilePathLastElement(mypath):
    return mypath.split("\\")[-1]

# Function 10: check the same script name
def checkSameScriptName(sql_file_list):
    filtered_list=[]
    sql_file_list=getFileNameOnly(sql_file_list)
    for sql_file in sql_file_list:
        if sql_file_list.count(sql_file) > 1:
            filtered_list.append(sql_file)
    return filtered_list

# Function 11: check space in filename
def checkFileNameSpace(sql_file_list):
    filtered_list=[]
    sql_file_list=getFileNameOnly(sql_file_list)
    for sql_file in sql_file_list:
        if not sql_file.split(" ",)[0].endswith((".sql",".ppm",".aat",".pps",".prd")):
            filtered_list.append(sql_file)
    return filtered_list

# Function 12: check missing env script
def checkMissingEnvFiles(sql_file_list):
    filtered_list=[]
    all_env_list=[]
    env_only_list=[]
    sql_name_list=[]
    repeated_sql_name_list=[]
    for sql_file in sql_file_list:
        # if (sql_file.endswith((".ppm",".aat",".pps",".prd")) >= 1) and ((sql_file.endswith(".ppm") < 1) or (sql_file.endswith(".aat") < 1) or (sql_file.endswith(".pps") < 1) or ((sql_file.endswith(".prd") < 1))):
        # if ((sql_file.endswith(".ppm") < 1) or (sql_file.endswith(".aat") < 1) or (sql_file.endswith(".pps") < 1) or ((sql_file.endswith(".prd") < 1))):
        if sql_file.endswith((".ppm",".aat",".pps",".prd")):
            all_env_list.append(sql_file)
    
    all_env_list = getFileName(all_env_list)
    # all_env_list = set(all_env_list)
    if len(all_env_list) >= 1: 
        for env_file in all_env_list:
            env_only_list.append(env_file.split(".sql.")[1])

        for env_file in all_env_list:
            sql_name_list.append(env_file.split(".sql.")[0])
    
    for sql_name_file in sql_name_list:
        if sql_name_list.count(sql_name_file) > 1:
            repeated_sql_name_list.append(sql_name_file)
    
    # if ("ppm" not in env_only_list) or ("aat" not in env_only_list) or ("pps" not in env_only_list) or ("prd" not in env_only_list):
    if len(repeated_sql_name_list) % 4 != 0:
        return all_env_list
    else:
        all_env_list=[]
        return all_env_list

# Function 13: get exception list 
def getExceptionList(file_list):
    filtered_list=[]
    file_list=getFileName(file_list)
    for file in file_list:
        if not file.endswith((".sql",".ppm",".aat",".pps",".prd")):
            filtered_list.append(file)
    return filtered_list

def checkChineseChar(sql_file_list):
    filtered_list=[]

    for sql_file in sql_file_list:
        with open(sql_file, 'r', errors='ignore') as file:
            file = file.read()
            if re.search('[\u4e00-\u9fff]', file):
                filtered_list.append(sql_file)
    filtered_list=getFileName(filtered_list)
    return filtered_list





  



        








    




