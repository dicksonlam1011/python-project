import datetime
import os
import operator

# ppm_sharefolder_path="//dc7shdns02b/CSC1/TEAMFOLDER/PPM"
# # month_path=input("Please enter the PPM Month folder (eg: 2021_12): \n")
# # ppm_folder=input("Please enter the PPM Folder Name (eg: 2021-S0492(K2)): \n")
# month_path="2021_12"
# ppm_folder="Dickson_test"
# mypath="{}/{}/{}".format(ppm_sharefolder_path, month_path, ppm_folder)
mypath=input("Plesae input the PPM source path:"+"\n")

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

# get the last 4 element in the file path list
def getFileName(sql_file_list):
    temp_list=[]
    file_path=[]
    for sql_file in sql_file_list:
        file_path.append('/'.join(map(str, sql_file.split("\\")[-4:])))
    return file_path

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

    filename_list=getFileName(getAllSqlFileList())
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

    return getFileName(checkHospcodeResult)

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
    

    file = open(os.path.join(mypath,"scanning_result.log"), mode="w",encoding="utf8")
    header_scan=checkSybaseHeader(getAllSqlFileList())
    basic_syntax_scan=checkSybaseBasicSyntax(getAllSqlFileList(),"go")
    corp_hospcode_scan=checkSybaseHospcode(getSpecificTypeSqlFilelist("_corp-db_"),"##hospcode##")
    hosp_hospcode_scan=checkSybaseHospcode(getSpecificTypeSqlFilelist("_imp-corp-db_"),"HAH" )
    corp7_menu_function_list_scan=checkScriptSpecialIssues(getAllSqlFileList(),"menu_function_list")
    alter_script_scan=checkUnsupportedScript(getAllSqlFileList(),"alter table")
    local_moe_manual_content_scan=checkSybaseBasicSyntax(getSpecificTypeSqlFilelist("LOCAL_MOE"), "XXXmoe_db")
    loe_manual_scan=checkFilePath(getAllSqlFileList(),"LOE","_manual_")
    local_moe_manual_scan=checkFilePath(getAllSqlFileList(),"LOCAL_MOE","_manual_")

    file.write("Scanning 1: =================Header scanning result====================="+"\n")
    if len(header_scan)>=1:
        file.write("==> The following script(s) Header Information (script name) does NOT matched with the source"+"\n")
        for result in header_scan:
            # file.write(result+": Header Result Failed!! "+"\n")
            file.write(result+"\n")
    else:
        file.write("Scanned script header information PASS"+"\n")



    file.write("\n"+"Scanning 2: =================Syntax scanning result====================="+"\n")
    if len(basic_syntax_scan)>=1:
        file.write("==> The following script(s) missing 'GO' in the scripts"+"\n")
        for result in basic_syntax_scan:
                # file.write(result+": Go is missing in the script !! "+"\n")
                file.write(result+"\n")
    else:
        file.write("Scanned script syntax information PASS"+"\n")


    file.write("\n"+"Scanning 3: =================Central/Hospital E-form variable scanning result====================="+"\n") 
    if len(corp_hospcode_scan)>=1:
        file.write("==> The following script(s) occurred E-form variables mistables "+"\n")
        for result in corp_hospcode_scan:
            # file.write(result+": Central script variable mistake!! "+"\n")
            file.write(result+"\n")
        for result in hosp_hospcode_scan:
            # file.write(result+": Hospital script variable mistake!! "+"\n")
            file.write(result+"\n")
    else:
        file.write("Scanned script e-form variable PASS"+"\n")


    file.write("\n"+"Scanning 4: =================Corp 7 menu function list scanning result====================="+"\n") 
    if len(corp7_menu_function_list_scan)>=1:
        file.write("==> The following script(s) involve CORP7 menu function list, please check the E-form setup information for the step of refresh cache"+"\n")
        for result in corp7_menu_function_list_scan:
            # file.write(result+": Scanned presence of CORP7 menu function list script, please state refresh cache step in promotion form "+"\n")
            file.write(result+"\n")
    else:
        file.write("Scanned No CORP7 menu function list included"+"\n")


    file.write("\n"+"Scanning 5: =================Alter scripts scanning result====================="+"\n") 
    if len(alter_script_scan)>=1:
        file.write("==> The following script(s) of Alter Tables are NOT set to be manual types"+"\n")
        for result in alter_script_scan:
            # file.write(result+": Scanned alter scripts are NOT set to be manual workflow"+"\n")
            file.write(result+"\n")
    else:
        file.write("Scanned no alter scripts set to be wrong source type"+"\n")


    file.write("\n"+"Scanning 6: =================Local MOE scripts scanning result====================="+"\n") 
    if len(local_moe_manual_content_scan)>=1:
        file.write("==> The following local moe script(s) missing 'XXXmoe_db' in PPM"+"\n")
        for result in local_moe_manual_content_scan:
            file.write(result+": Scanned local moe imp-manual scripts no XXXmoe_db"+"\n")
    else:
        file.write("Scanned manual local moe script PASS"+"\n")


    file.write("\n"+"Scanning 7: =================Manual types of LOE and Local MOE scripts scanning result====================="+"\n") 
    if len(loe_manual_scan)>=1:
        file.write("==> The following local moe/LOE script(s) are set to wrong source type"+"\n")
        for result in loe_manual_scan:
            # file.write(result+": Scanned Loe/ local moe manual-workflow script wrong script type"+"\n")
            file.write(result+"\n")
        for result in local_moe_manual_scan:
            # file.write(result+": Scanned Loe/ local moe manual-workflow script wrong script type"+"\n")
            file.write(result+"\n")
    else:
        file.write("Scanned loe/local moe script source type PASS"+"\n")

        
    file.close()

OutputResult()
        

# def runCodeScanner():
# print(checkSybaseHeader(getAllSqlFileList(), getAllSqlNameList()))
# print(checkSybaseBasicSyntax(getAllSqlFileList(), "go", "GO"))
# print(checkSybaseHospcode(getSpecificTypeSqlFilelist("_manual_"),"HAH"))
# print(checkSybaseHospcode(getSpecificTypeSqlFilelist("_manual_"),"hospcode"))


# runCodeScanner()







        








    




