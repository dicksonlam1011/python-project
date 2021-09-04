import datetime
import pandas as pd
import numpy as np
from pandas.core.algorithms import isin
import PPM_Summary_excel as summary
import os


print("Start Python Project!")
##############################################################


# ppm_summary = pd.ExcelFile('python-project-source/promotion_summary_2021_Backup.xls')
# # bi_weekly=pd.read_excel(ppm_summary, 'Bi-weekly')
# # urgent = pd.read_excel(ppm_summary, 'Urgent')
# # service = pd.read_excel(ppm_summary, 'Service')

# ####################################################################################
# filter_last_BW=input("Enter the last Release Day in YYYY-MM-DD format: ")
# year1, month1, day1 = map(int, filter_last_BW.split("-"))
# filter_last_BW=datetime.datetime(year1, month1, day1)

# filter_next_BW=input("Enter the next BW Release Day in YYYY-MM-DD format: ")
# year2, month2, day2 = map(int, filter_next_BW.split("-"))
# filter_next_BW=datetime.datetime(year2, month2, day2)

# BW_releaseSch=input("Enter the BW Release Schedule in XXXX-MM formart: ")
# ####################################################################################



# filter_datetime=urgent["Ready for Promotion"].apply(type)==datetime.datetime
# condition= (pd.isna(urgent["Serial no."])==False) & (urgent[filter_datetime]["Ready for Promotion"]>=filter_last_BW) & (urgent[filter_datetime]["Ready for Promotion"]<filter_next_BW) 
# print(urgent[condition]["Ready for Promotion"])


# # Ouput to date.txt
BW=summary.getBiWeeklyData()
Urg=summary.getUrgentData()
SV=summary.getServiceData()



# all_jira=summary.getJiraData(BW)+summary.getJiraData(Urg)+summary.getJiraData(SV)
all_jiraList=summary.getFunctionList(BW)+summary.getFunctionList(Urg)+summary.getFunctionList(SV)
filtered_jiraList=summary.getFunctionData(BW)+summary.getFunctionData(Urg)+summary.getFunctionData(SV)
dict={}
for count in filtered_jiraList:
    # print(count, all_jiraList.count(count))
    dict.update({count:all_jiraList.count(count)})
# print(dict)
dict={ k:v for k,v in sorted(dict.items(),key=lambda item: item[1], reverse=True)}
print(dict)


# >>> x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# >>> {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
# {0: 0, 2: 1, 1: 2, 4: 3, 3: 4}




# Ouput to date.txt

# BW_releaseSch=input("Enter the BW Release Schedule in XXXX-MM formart: ")
# # year3, month3 = map(int, BW_releaseSch.split("-"))

# # with open(os.path.join('/path/to/Documents',completeName), "w") as file1:

# # with open("python-project-source/{}/BW-{}.csv".format(BW_releaseSch, BW_releaseSch), mode="w",encoding="utf8") as file: # Open a file
# #     if not os.path.isdir("Urg-{}.csv".format(BW_releaseSch)):
# #         os.mkdir("Urg-{}.csv".format(BW_releaseSch))
# if not os.path.isdir("{}".format(BW_releaseSch)):
#     os.mkdir("{}".format(BW_releaseSch))

# with open( os.path.join("{}".format(BW_releaseSch),"BW-{}.csv".format(BW_releaseSch)), mode="w",encoding="utf8") as file: # Open a file
#     data=BW.to_string()
#     file.write(data)

# with open(os.path.join("{}".format(BW_releaseSch),"Urg-{}.csv".format(BW_releaseSch)), mode="w",encoding="utf8") as file: # Open a file
#     data=Urg.to_string()
#     file.write(data)

# with open(os.path.join("{}".format(BW_releaseSch),"SV-{}.csv".format(BW_releaseSch)), mode="w",encoding="utf8") as file: # Open a file
#     data=SV.to_string()
#     file.write(data)

# print(urgent["Ready for Promotion"])

# print(bi_weekly["Ready for Promotion"])

# datetime_list=[]
# for col in bi_weekly["Ready for Promotion"].items():
#     if type(col[1]) == datetime.datetime:
#         datetime_list.append(col[1])
# print(datetime_list)

# filter_datetime=bi_weekly["Ready for Promotion"]
# filter_datetime=isinstance(bi_weekly["Ready for Promotion"],datetime.datetime)
# filter_datetime=bi_weekly["Ready for Promotion"].apply(type)==datetime.datetime
# # filter_datetime=bi_weekly["Ready for Promotion"][bi_weekly["Ready for Promotion"].apply(lambda xxx: isinstance(xxx, datetime.datetime))]

# condition= (pd.isna(bi_weekly["Serial no."])==False) & (bi_weekly["Ready for Promotion"].apply(type)==datetime.datetime) & (bi_weekly["Ready for Promotion"]>=filter_last_BW) & (bi_weekly["Ready for Promotion"]<filter_next_BW) 

# pd.to_datetime(bi_weekly["Ready for Promotion"],errors="coerce")
# print(bi_weekly["Ready for Promotion"])
# filter_datetime=bi_weekly["Ready for Promotion"].apply(type)==datetime.datetime
# condition= (pd.isna(bi_weekly["Serial no."])==False) & (bi_weekly["Ready for Promotion"]>=filter_last_BW) 
# # & (bi_weekly["Ready for Promotion"]>=filter_last_BW) & (bi_weekly["Ready for Promotion"]<filter_next_BW) 

# # (bi_weekly["Ready for Promotion"]>=filter_last_BW) & (bi_weekly["Ready for Promotion"]<filter_next_BW)
# # bi_weekly["Ready for Promotion"]
# # print(bi_weekly.select_dtypes(include=['datetime64']).columns)
# # print(bi_weekly[condition])
# print(bi_weekly[condition])

# condition=(filter_datetime>=filter_last_BW) & (filter_datetime<filter_next_BW) & (pd.isna(bi_weekly["Serial no."])==False) 
# print(bi_weekly[condition])
# print(filter_datetime)clea
# print(filter_datetime)
# condition=(filter_datetime>=filter_last_BW) & (filter_datetime<filter_next_BW) & (pd.isna(bi_weekly["Serial no."])==False) 

# filter_data=bi_weekly["Ready for Promotion"].apply(type)==datetime.datetime
# # print(bi_weekly[filter_data])

# condition = (pd.isna(bi_weekly["Serial no."])==False) & (bi_weekly[filter_data]["Ready for Promotion"]>=filter_last_BW) & (bi_weekly[filter_data]["Ready for Promotion"]<filter_next_BW)

# print(bi_weekly[condition])

# print(bi_weekly["Ready for Promotion"])
# condition=(pd.isna(bi_weekly["Serial no."])==False) & (BW_datetime[BW_datetime.apply(lambda x: isinstance(x, datetime.datetime))])
# condition=BW_datetime[BW_datetime.apply(lambda x: isinstance(x, datetime.datetime))]
# print(bi_weekly[condition])

# & (pd.bi_weekly["Ready for Promotion"].str.contains("(1)"))
# (pd.to_datetime(bi_weekly["Ready for Promotion"], errors='ignore'))



# # # Ouput to date.txt
# with open("data.txt", mode="w",encoding="utf8") as file: # Open a file
#     data=bi_weekly["Ready for Promotion"].to_string()
#     file.write(data)

# condition=(pd.isna(bi_weekly["Ready for Promotion"])==False)

# (bi_weekly["Ready for Promotion"].astype("datetime64[ns]"))
# (pd.to_datetime(bi_weekly["Ready for Promotion"]))


# print(bi_weekly[condition]["Ready for Promotion"])
# print(type(bi_weekly[condition]["Ready for Promotion"]))
# for col in bi_weekly[condition]["Ready for Promotion"].items():
#     for data in col:
#         if type(data) == datetime.datetime:
#             # print(type(data))
#             print(data)




