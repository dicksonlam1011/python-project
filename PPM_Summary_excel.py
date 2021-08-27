import pandas as pd
import datetime

### Part 1: Get Data from Summary Sheet
ppm_summary = pd.ExcelFile('python-project-source/promotion_summary_2021_Backup.xls')

### Part 2: Specify the Sheet Tab
bi_weekly=pd.read_excel(ppm_summary, 'Bi-weekly')
urgent = pd.read_excel(ppm_summary, 'Urgent')
service = pd.read_excel(ppm_summary, 'Service')
# urgent=urgent.to_dict()

### Part 3: Observe the Sheet tab Information
# print(urgent)
# print("Data Number", urgent.size)
# print("Data Shape (row, column)", urgent.shape)
# print("Data Index", urgent.columns)


# ### Par 4: Data Filtering
# filter_last_BW=input("Enter the last Release Day in YYYY-MM-DD format: ")
# year1, month1, day1 = map(int, filter_last_BW.split("-"))
# filter_last_BW=datetime.datetime(year1, month1, day1)

# filter_next_BW=input("Enter the next BW Release Day in YYYY-MM-DD format: ")
# year2, month2, day2 = map(int, filter_next_BW.split("-"))
# filter_next_BW=datetime.datetime(year2, month2, day2)

def getBiWeeklyData():
    condition=(bi_weekly["Ready for Promotion"]>filter_last_BW) & (bi_weekly["Ready for Promotion"]<filter_next_BW)
    # print(urgent[condition])
    return bi_weekly[condition]

def getUrgentData():
    condition=(urgent["Ready for Promotion"]>filter_last_BW) & (urgent["Ready for Promotion"]<filter_next_BW)
    # print(urgent[condition])
    return urgent[condition]

def getServiceData():
    condition=(service["Ready for Promotion"]>filter_last_BW) & (service["Ready for Promotion"]<filter_next_BW)
    # print(urgent[condition])
    return service[condition]

# print(getBiWeeklyData())
# print(getUrgentData())
# print(getServiceData())

# print(bi_weekly["Ready for Promotion"])
for result in bi_weekly["Ready for Promotion"]:
   if type(result) is str:
       print(result)





