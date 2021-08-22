import pandas as pd
import datetime


ppm_summary = pd.ExcelFile('python-project-source/promotion_summary_2021.xls')
# bi_weekly_sheet = pd.read_excel(ppm_summary, 'Bi-weekly')
urgent = pd.read_excel(ppm_summary, 'Urgent')
# service = pd.read_excel(ppm_summary, 'Service')

# print(bi_weekly_sheet)
# print("Data Number", bi_weekly_sheet.size)
# print("Data Shape (row, column)", bi_weekly_sheet.shape)
# print("Data Index", bi_weekly_sheet.index)

# BW_07=datetime.datetime(2021,7,5)
# for UtargetDate in urgent["Ready for Promotion"]:
#     if (type(UtargetDate) is datetime.datetime) and UtargetDate >= BW_07: 
#             print(UtargetDate)
list1=[1,2,3]
BW_07_date=datetime.datetime(2021,7,5)
condition=(type(list1) is datetime.datetime)
print(condition)
# filteredData=urgent[condition]
# print(filteredData)
