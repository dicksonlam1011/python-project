import sybase_code_scanner_functions as function
import os

mypath=input("Plesae input the PPM source path:"+"\n")

def RunCodeScanner(mypath):


    # Call Function
    file = open(os.path.join(mypath,"scanning_result.log"), mode="w",encoding="utf8")
    header_scan=function.checkSybaseHeader(function.getAllSqlFileList(mypath), mypath)
    basic_syntax_scan=function.checkSybaseBasicSyntax(function.getAllSqlFileList(mypath),"Go")
    corp_hospcode_scan=function.checkSybaseHospcode(function.getSpecificTypeSqlFilelist(mypath, "_corp-db_"),"##hospcode##")
    hosp_hospcode_scan=function.checkSybaseHospcode(function.getSpecificTypeSqlFilelist(mypath, "_imp-corp-db_"),"HAH" )
    corp7_menu_function_list_scan=function.checkScriptSpecialIssues(function.getAllSqlFileList(mypath),"menu_function_list")
    alter_script_scan=function.checkUnsupportedScript(function.getAllSqlFileList(mypath),"alter table")
    db_option_scan=function.checkUnsupportedScript(function.getAllSqlFileList(mypath),"sp_dboption")
    local_moe_manual_content_scan=function.checkSybaseBasicSyntax(function.getSpecificTypeSqlFilelist(mypath, "LOCAL_MOE"), "XXXmoe_db")
    loe_manual_scan=function.checkFilePath(function.getAllSqlFileList(mypath),"LOE","_manual_")
    local_moe_manual_scan=function.checkFilePath(function.getAllSqlFileList(mypath),"LOCAL_MOE","_manual_")

    # Output log file
    file.write("\n"+"================================================================================================"+"\n") 
    file.write("================= Alert: Please request FPs to revise the following items =====================") 
    file.write("\n"+"================================================================================================"+"\n") 

    file.write("\n"+"Scanning 1: =================Syntax scanning result====================="+"\n")
    if len(basic_syntax_scan)>=1:
        file.write("==> The following script(s) missing 'GO' in the scripts"+"\n")
        for result in basic_syntax_scan:
                # file.write(result+": Go is missing in the script !! "+"\n")
                file.write(result+"\n")
    else:
        file.write("Scanned script syntax information PASS"+"\n")


    file.write("\n"+"Scanning 2: =================Central/Hospital E-form variable scanning result====================="+"\n") 
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

    file.write("\n"+"Scanning 3: =================Alter scripts scanning result====================="+"\n") 
    if len(alter_script_scan)>=1:
        file.write("==> The following script(s) of Alter Tables are NOT set to be manual types"+"\n")
        for result in alter_script_scan:
            # file.write(result+": Scanned alter scripts are NOT set to be manual workflow"+"\n")
            file.write(result+"\n")
        for result in db_option_scan:
            # file.write(result+": Scanned alter scripts are NOT set to be manual workflow"+"\n")
            file.write(result+"\n")
    else:
        file.write("Scanned no alter scripts set to be wrong source type"+"\n")


    file.write("\n"+"Scanning 4: =================Local MOE scripts scanning result====================="+"\n") 
    if len(local_moe_manual_content_scan)>=1:
        file.write("==> The following local moe script(s) missing 'XXXmoe_db' in PPM"+"\n")
        for result in local_moe_manual_content_scan:
            file.write(result+": Scanned local moe imp-manual scripts no XXXmoe_db"+"\n")
    else:
        file.write("Scanned manual local moe script PASS"+"\n")


    file.write("\n"+"Scanning 5: =================Manual types of LOE and Local MOE scripts scanning result====================="+"\n") 
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

    file.write("\n"+"================================================================================================"+"\n") 
    file.write("================= Warning: Please remind FPs to update the following items =====================") 
    file.write("\n"+"================================================================================================"+"\n") 

    file.write("\n"+"Scanning 6: =================Header scanning result====================="+"\n")
    if len(header_scan)>=1:
        file.write("==> The following script(s) Header Information (script name) does NOT matched with the source"+"\n")
        for result in header_scan:
            # file.write(result+": Header Result Failed!! "+"\n")
            file.write(result+"\n")
    else:
        file.write("Scanned script header information PASS"+"\n")

    file.write("\n"+"Scanning 7: =================Corp 7 menu function list scanning result====================="+"\n") 
    if len(corp7_menu_function_list_scan)>=1:
        file.write("==> The following script(s) involve CORP7 menu function list, please check the E-form setup information for the step of refresh cache"+"\n")
        for result in corp7_menu_function_list_scan:
            # file.write(result+": Scanned presence of CORP7 menu function list script, please state refresh cache step in promotion form "+"\n")
            file.write(result+"\n")
    else:
        file.write("Scanned No CORP7 menu function list included"+"\n")
        
    file.close()

RunCodeScanner(mypath)