import datetime
import pandas as pd
import numpy as np


print("Start Python Project!")
##############################################################


ppm_summary = pd.ExcelFile('python-project-source/promotion_summary_2021_Backup.xls')
bi_weekly=pd.read_excel(ppm_summary, 'Bi-weekly')
pd.to_datetime(bi_weekly["Ready for Promotion"], errors='coerce')
# print(bi_weekly["Ready for Promotion"])


# Ouput to date.txt
with open("data.txt", mode="w",encoding="utf8") as file: # Open a file
    data=bi_weekly["Ready for Promotion"].to_string()
    file.write(data)

# condition=(pd.isna(bi_weekly["Ready for Promotion"])==False)

# print(bi_weekly[condition]["Ready for Promotion"])
# (bi_weekly["Ready for Promotion"].astype("datetime64[ns]"))
# (pd.to_datetime(bi_weekly["Ready for Promotion"]))


# print(bi_weekly[condition]["Ready for Promotion"])
# print(type(bi_weekly[condition]["Ready for Promotion"]))
# for col in bi_weekly[condition]["Ready for Promotion"].items():
#     for data in col:
#         if type(data) == datetime.datetime:
#             # print(type(data))
#             print(data)




