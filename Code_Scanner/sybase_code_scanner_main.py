import sybase_code_scanner_functions as function
import os

mypath=input("Plesae input the PPM source path:"+"\n")

def RunCodeScanner(mypath):


    # Call Function
    file = open(os.path.join(mypath,"{}_scanning_result.log".format(function.getfilePathLastElement(mypath))), mode="w",encoding="utf8")
    headerName_scan=function.checkSybaseHeader(function.getAllSqlFileList(mypath), mypath)
    header_scan_1=function.checkSybaseBasicSyntax(function.getAllSqlFileList(mypath),"/*")
    # header_scan_2=function.checkSybaseBasicSyntax(function.getAllSqlFileList(mypath),"*/")
    basic_syntax_scan=function.checkLastLine(function.getAllSqlFileList(mypath),"Go")
    same_script_name_scan=function.checkSameScriptName(function.getAllSqlFileList(mypath))
    space_script_name_scan=function.checkFileNameSpace(function.getAllSqlFileList(mypath))
    corp_hospcode_scan=function.checkSybaseHospcode(function.getSpecificTypeSqlFilelist("_corp-db_", mypath),"##hospcode")
    hosp_hospcode_scan=function.checkSybaseHospcode(function.getSpecificTypeSqlFilelist("_imp-corp-db_", mypath),"HAH" )
    env_missing_scan=function.checkMissingEnvFiles(function.getAllSqlFileList(mypath))
    corp7_menu_function_list_scan=function.checkScriptSpecialIssues(function.getAllSqlFileList(mypath),"menu_function_list")
    alter_script_scan=function.checkUnsupportedScript(function.getAllSqlFileList(mypath),"alter table")
    db_option_scan=function.checkUnsupportedScript(function.getAllSqlFileList(mypath),"sp_dboption")
    local_moe_manual_content_scan=function.checkSybaseBasicSyntax(function.getSpecificTypeCheckingSqlFilelist("LOCAL_MOE", "_imp-manual_" , mypath), "XXXmoe_db")
    loe_manual_scan=function.checkFilePath(function.getAllSqlFileList(mypath),"LOE","_manual_")
    local_moe_manual_scan=function.checkFilePath(function.getAllSqlFileList(mypath),"LOCAL_MOE","_manual_")
    manual_script_syntax=function.checkSybaseBasicSyntax(function.getSpecificTypeSqlFilelist("_manual_", mypath), "use")
    imp_manual_script_syntax=function.checkSybaseBasicSyntax(function.getSpecificTypeSqlFilelist("_imp-manual_", mypath), "use")
    drop_table_scan=function.checkUnsupportedScript(function.getAllSqlFileList(mypath),"drop table")
    exception_list=function.getExceptionList(function.getAllFileList(mypath))
    chinese_sql_list=function.checkChineseChar(function.getAllSqlFileList(mypath))
    imp_corp_scan_hospital_variable=function.checkSybaseBasicSyntax(function.getSpecificTypeSqlFilelist("_imp-corp-db_", mypath), "##hospcode")



    # Output log file
    file.write(">>> scanned: "+ function.getfilePathLastElement(mypath) +" <<<"+"\n"+"\n")

    file.write("\n"+"================================================================================================"+"\n") 
    file.write("================= Alert: Please request FPs to revise the following items =====================") 
    file.write("\n"+"================================================================================================"+"\n") 

    if len(basic_syntax_scan)>=1:
        file.write("\n"+"Alert 1: =================Syntax scanning result====================="+"\n")
        file.write("The following script(s) does not end with 'GO' in the scripts"+"\n")
        for result in basic_syntax_scan:
                # file.write(result+": Go is missing in the script !! "+"\n")
                file.write(result+"\n")
    else:
        file.write("PASS: script syntax scanning okay"+"\n")

    if (len(corp_hospcode_scan) >=1) or (len(hosp_hospcode_scan) >=1):
        file.write("\n"+"Alert 2: =================Central/Hospital E-form variable scanning result====================="+"\n") 
        file.write("The following script(s) occurred E-form variables mistables "+"\n")
        for result in corp_hospcode_scan:
            # file.write(result+": Central script variable mistake!! "+"\n")
            file.write(result+"\n")
        for result in hosp_hospcode_scan:
            # file.write(result+": Hospital script variable mistake!! "+"\n")
            file.write(result+"\n")
    else:
        file.write("PASS: e-form variable scanning okay"+"\n")

    if (len(alter_script_scan)>=1) or (len(db_option_scan)>=1):
        file.write("\n"+"Alert 3: =================Alter scripts scanning result====================="+"\n") 
        file.write("The following script(s) of Alter Tables are NOT set to be manual types"+"\n")
        for result in alter_script_scan:
            # file.write(result+": Scanned alter scripts are NOT set to be manual workflow"+"\n")
            file.write(result+"\n")
        for result in db_option_scan:
            # file.write(result+": Scanned alter scripts are NOT set to be manual workflow"+"\n")
            file.write(result+"\n")
    else:
        file.write("PASS: alter scripts scanning okay"+"\n")


    if len(local_moe_manual_content_scan)>=1:
        file.write("\n"+"Alert 4: =================Local MOE scripts scanning result====================="+"\n") 
        file.write("The following local moe script(s) missing 'XXXmoe_db' in PPM"+"\n")
        for result in local_moe_manual_content_scan:
            file.write(result+"\n")
    else:
        file.write("PASS: manual local moe script scanning okay"+"\n")


    if (len(loe_manual_scan)>=1) or (len(local_moe_manual_scan)>=1):
        file.write("\n"+"Alert 5: =================Manual types of LOE and Local MOE scripts scanning result====================="+"\n") 
        file.write("The following local moe/LOE script(s) are set to wrong source type"+"\n")
        for result in loe_manual_scan:
            # file.write(result+": Scanned Loe/ local moe manual-workflow script wrong script type"+"\n")
            file.write(result+"\n")
        for result in local_moe_manual_scan:
            # file.write(result+": Scanned Loe/ local moe manual-workflow script wrong script type"+"\n")
            file.write(result+"\n")
    else:
        file.write("PASS: loe or local moe script source type scanning okay"+"\n")
    
     
    if (len(manual_script_syntax)>=1) or (len(imp_manual_script_syntax) >=1):
        file.write("\n"+"Alert 6: ================= Manual types of scripts syntax scanning result ====================="+"\n")
        file.write("The following manual scripts missing use db, go"+"\n")
        for result in manual_script_syntax:
            # file.write(result+": Scanned Loe/ local moe manual-workflow script wrong script type"+"\n")
            file.write(result+"\n")
        for result in imp_manual_script_syntax:
            # file.write(result+": Scanned Loe/ local moe manual-workflow script wrong script type"+"\n")
            file.write(result+"\n")
    else:
        file.write("PASS: manual script syntax scanning okay"+"\n")
    
     
    if len(drop_table_scan)>=1:
        file.write("\n"+"Alert 7: ================= Drop Table script scanning result ====================="+"\n")
        file.write("The following drop table scripts are not set to be manual scripts"+"\n")
        for result in drop_table_scan:
            # file.write(result+": Scanned Loe/ local moe manual-workflow script wrong script type"+"\n")
            file.write(result+"\n")
    else:
        file.write("PASS: drop table script scanning okay"+"\n")
    
    if len(env_missing_scan)>=1:
        file.write("\n"+"Alert 8: ================= All Env scripts scanning result ====================="+"\n")
        file.write("The following sql files missing at least one environment version"+"\n")
        for result in env_missing_scan:
            # file.write(result+": Scanned Loe/ local moe manual-workflow script wrong script type"+"\n")
            file.write(result+"\n")
    else:
        file.write("PASS: all env scripts scanned okay"+"\n")

    if len(imp_corp_scan_hospital_variable)>=1:
        file.write("\n"+"Alert 9: ================= IMP CORP script scanning result ====================="+"\n")
        file.write("The following sql files missing E-form hospital variables in the content"+"\n")
        for result in imp_corp_scan_hospital_variable:
            file.write(result+"\n")
    else:
        file.write("PASS: all imp-corp-db scripts scanned okay"+"\n")


    file.write("\n"+"================================================================================================"+"\n") 
    file.write("================= Warning: Please remind FPs to update the following items =====================") 
    file.write("\n"+"================================================================================================"+"\n") 

    
    if (len(header_scan_1)>=1):
        file.write("\n"+"Warning 1: =================Header scanning result====================="+"\n")
        file.write("The following script(s) missing Header Information"+"\n")
        for result in header_scan_1:
            # file.write(result+": Header Result Failed!! "+"\n")
            file.write(result+"\n")
    else:
        file.write("PASS: script header information scanning okay"+"\n")
    
        
    if len(headerName_scan)>=1:
        file.write("\n"+"Warning 2: =================Header Script Name scanning result====================="+"\n")
        file.write("The following script(s) Header Information (script name) does NOT matched with the source"+"\n")
        for result in headerName_scan:
            # file.write(result+": Header Result Failed!! "+"\n")
            file.write(result+"\n")
    else:
        file.write("PASS: script header script name scanning okay"+"\n")

     
    if len(corp7_menu_function_list_scan)>=1:
        file.write("\n"+"Warning 3: =================Corp 7 menu function list scanning result====================="+"\n")
        file.write("The following script(s) involve CORP7 menu function list, please check the E-form setup information for the step of refresh cache"+"\n")
        for result in corp7_menu_function_list_scan:
            # file.write(result+": Scanned presence of CORP7 menu function list script, please state refresh cache step in promotion form "+"\n")
            file.write(result+"\n")
    else:
        file.write("PASS: no CORP7 menu function list included"+"\n")

     
    if len(same_script_name_scan)>=1:
        file.write("\n"+"Warning 4: ================= SQL file name uniqueness scanning result ====================="+"\n")
        file.write("The following script(s) have the same script names"+"\n")
        for result in same_script_name_scan:
            # file.write(result+": Scanned presence of CORP7 menu function list script, please state refresh cache step in promotion form "+"\n")
            file.write(result+"\n")
    else:
        file.write("PASS: all filenames are unique"+"\n")
    
     
    if len(space_script_name_scan)>=1:
        file.write("\n"+"Warning 5: ================= SQL file name white space scanning result ====================="+"\n")
        file.write("The following script(s) have the while space in filename"+"\n")
        for result in space_script_name_scan:
            # file.write(result+": Scanned presence of CORP7 menu function list script, please state refresh cache step in promotion form "+"\n")
            file.write(result+"\n")
    else:
        file.write("PASS: no while space found in filenames"+"\n")
    
    if len(chinese_sql_list)>=1:
        file.write("\n"+"Warning 6: ================= Chinese character scanning result ====================="+"\n")
        file.write("The following script(s) involve chinese characters in the content, please mention in setup information" + "\n")
        for result in chinese_sql_list:
            # file.write(result+": Scanned presence of CORP7 menu function list script, please state refresh cache step in promotion form "+"\n")
            file.write(result+"\n")
    else:
        file.write("PASS: no chinese character found"+"\n")
    
    if len(exception_list) > 1:
        file.write("\n"+"================================================================================================"+"\n") 
        file.write("================= Exception List: The following scripts are NOT scanned ====================="+"\n") 
        file.write("================= Please perform checking manually ====================="+"\n") 
        file.write("================================================================================================"+"\n") 
        for result in exception_list:
            file.write(result+"\n")            
    file.close()

# !!! execute the code scanner
RunCodeScanner(mypath)



# print("Test GitHub Branches Administration")




