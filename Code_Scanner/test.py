import re


# text = "./data/NCDC/上海/虹桥/9705626661750dat.txt"
# text2 = "./data/NCDC/ciampino/6240476818161dat.txt"

# if re.search("[\u4e00-\u9fff]", text2):
#     print("found chinese character")
# else:
#     print("Pass")


# sql_file='C:/PPM_Deployment_Preparation/Dickson_test_bad_cases/DP_180_corp-db_UpdateConfig/DB_SERVER_LIST_CORP3/corp/010_TELECARE-34_insert_config.sql'
sql_file='C:/PPM_Deployment_Preparation/Dickson_test_bad_cases/DP_180_corp-db_UpdateConfig/DB_SERVER_LIST_CORP3/corp/chinese.sql'
with open(sql_file, 'r', encoding="utf-8", errors='ignore') as file:
    file=file.read()
    if re.search('[\u4e00-\u9fff]', file):
        print('found chinese character in ' + sql_file)
    else:
        print('Pass')