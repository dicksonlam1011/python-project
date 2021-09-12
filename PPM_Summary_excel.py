from numpy import datetime_data, string_
import pandas as pd
import datetime
import os
import json

### Part 1: Get Data from Summary Sheet
# Get sample source from local file
ppm_summary = pd.ExcelFile('python-project-source/promotion_summary_2021_Backup.xls')
relese_schedule = pd.ExcelFile("python-project-source/Deployment_release_schedule_Backup.xlsx")

# Get real source from shared folder
# ppm_summary = pd.ExcelFile("//hocmsf1/CSC1/CMS_promote/Summary/Backup/Summary_for_Statistics/promotion_summary_2021_Backup.xls")
# relese_schedule = pd.ExcelFile("//hocmsf1/CSC1/CMS_promote/Summary/Backup/Summary_for_Statistics/Deployment_release_schedule_Backup.xlsx")

### Part 2: Specify the Sheet Tab
bi_weekly=pd.read_excel(ppm_summary, 'Bi-weekly')
urgent = pd.read_excel(ppm_summary, 'Urgent')
service = pd.read_excel(ppm_summary, 'Service')
prd_release = pd.read_excel(relese_schedule)
# urgent=urgent.to_dict()

### Part 3: Observe the Sheet tab Information
# print(urgent)
# print("Data Number", urgent.size)
# print("Data Shape (row, column)", urgent.shape)
# print("Data Index", urgent.columns)

# ### Par 4: Data Filtering
try:
    filter_last_BW=input("Enter the last Release Day in YYYY-MM-DD format: ")
    year1, month1, day1 = map(int, filter_last_BW.split("-"))
    filter_last_BW=datetime.datetime(year1, month1, day1)
except ValueError:
    raise ValueError("Incorrect data format, should be YYYY-MM-DD")

try:
    filter_next_BW=input("Enter the next BW Release Day in YYYY-MM-DD format: ")
    year2, month2, day2 = map(int, filter_next_BW.split("-"))
    filter_next_BW=datetime.datetime(year2, month2, day2)
except ValueError:
    raise ValueError("Incorrect data format, should be YYYY-MM-DD")

try:
    BW_releaseSch=input("Enter the BW Release Schedule in XXXX-MM formart: ")
    year3, month3 = map(int, BW_releaseSch.split("-"))
except ValueError:
    raise ValueError("Incorrect data format, should be YYYY-MM")

# get BW data by release day
def getBiWeeklyData():
    # pd.to_datetime(bi_weekly["Ready for Promotion"])
    filter_datetime=bi_weekly["Ready for Promotion"].apply(type)==datetime.datetime
    # condition=(bi_weekly["Ready for Promotion"]>=filter_last_BW) & (bi_weekly["Ready for Promotion"]<filter_next_BW) & (pd.isna(bi_weekly["Serial no."])==False) & (bi_weekly["Ready for Promotion"].apply(type)==datetime.datetime)
    condition= (pd.isna(bi_weekly["Serial no."])==False) & (bi_weekly[filter_datetime]["Ready for Promotion"]>=filter_last_BW) & (bi_weekly[filter_datetime]["Ready for Promotion"]<filter_next_BW)
    # print(urgent[condition])
    # if df['a'].dtype != np.number:
    return bi_weekly[condition]

# print(getBiWeeklyData())

# get Urg data by release day
def getUrgentData():
    filter_datetime=urgent["Ready for Promotion"].apply(type)==datetime.datetime
    condition= (pd.isna(urgent["Serial no."])==False) & (urgent[filter_datetime]["Ready for Promotion"]>=filter_last_BW) & (urgent[filter_datetime]["Ready for Promotion"]<filter_next_BW)
    # & (urgent["Ready for Promotion"].apply(type)==datetime.datetime)
    # print(urgent[condition])
    return urgent[condition]

# get SV data by release day
def getServiceData():
    filter_datetime=service["Ready for Promotion"].apply(type)==datetime.datetime
    condition= (pd.isna(service["Serial no."])==False) & (service[filter_datetime]["Ready for Promotion"]>=filter_last_BW) & (service[filter_datetime]["Ready for Promotion"]<filter_next_BW)
    # & (service["Ready for Promotion"].apply(type)==datetime.datetime)
    # print(urgent[condition])
    return service[condition]

# get Urg Fallback data by release day
def getFallbackData(data,request_type):
    # data=getBiWeeklyData()
    # request_type="AAT"
    condition=(data["Remarks"].str.contains("Test Failure", case=False, na=False) | data["Remarks"].str.contains("Withdrawn", case=False, na=False) | data["Remarks"].str.contains("Fallback", case=False, na=False)) & data["Remarks"].str.contains(request_type, case=False, na=False)
    # return data[condition]
    return data[condition]

# get all related PPM number BW+Urg+SV
def getPpmNumber():
    return (getBiWeeklyData(), getUrgentData(), getServiceData())

# get Jira Number into a list
def getJiraNumber(data):
    # data=getUrgentData()
    jiraList=[]
    data=data["Change Request #"].str.split(", ",expand = True)
    for col in data.columns:
        for index, row in data[col].items():
            if row != None:
                jiraList.append(row)
    # return jiraList
    return len(jiraList)

def getJiraData(data):
    # data=getUrgentData()
    jiraList=[]
    data=data["Change Request #"].str.split(", ",expand = True)
    for col in data.columns:
        for index, row in data[col].items():
            if row != None:
                jiraList.append(row)
    # return jiraList
    return jiraList

# get Function list
def getFunctionData(data):
    # data=getUrgentData()
    jiraList=[]
    data=data["Change Request #"].str.split(", ",expand = True)
    for col in data.columns:
        for index, row in data[col].items():
            if row != None:
                jiraList.append(row.split("-")[0])
    functionList=list(dict.fromkeys(jiraList)) # remove duplicate items in the list
    return functionList

def getCombinedFunctionList(BW,Urg,SV):
    # BW=getBiWeeklyData()
    # Urg=getUrgentData()
    # SV=getServiceData()
    combined_list=getFunctionData(BW)+getFunctionData(Urg)+getFunctionData(SV)
    combined_list=list(dict.fromkeys(combined_list)) # remove duplicate items in the list
    return combined_list

# get Function list
def getFunctionList(data):
    # data=getUrgentData()
    jiraList=[]
    data=data["Change Request #"].str.split(", ",expand = True)
    for col in data.columns:
        for index, row in data[col].items():
            if row != None:
                jiraList.append(row.split("-")[0])
    return jiraList

def getFunctionDataToImage(BW,Urg,SV):
    all_jiraList=getFunctionList(BW)+getFunctionList(Urg)+getFunctionList(SV)
    filtered_jiraList=getFunctionData(BW)+getFunctionData(Urg)+getFunctionData(SV)
    dict={}
    for count in filtered_jiraList:
        # print(count, all_jiraList.count(count))
        dict.update({count:all_jiraList.count(count)})
    # print(dict)
    dict={ k:v for k,v in sorted(dict.items(),key=lambda item: item[1], reverse=True)}
    # print("Function Number Involved for this batch of requests")
    # print(dict)
    if not os.path.isdir("{}".format(BW_releaseSch)):
        os.mkdir("{}".format(BW_releaseSch))

    with open(os.path.join("{}".format(BW_releaseSch),"FunctionDataToImage-{}.csv".format(BW_releaseSch)), mode="w",encoding="utf8") as file: # Open a file
        function_list=json.dump(dict, file)
        # data=json.dump(dict, file)
        # file.write(data)

        # import json

        # with open("config.json", mode="w",encoding="utf8") as file:
        #     json.dump(data, file)
        # print(data)


# get Ear list
def getEarData(data):
    # data=getUrgentData()
    # print(data["EAR file"])
    earList=[]
    data=data["EAR file"].str.split(", ",expand = True)
    # print(data)
    for col in data.columns:
        for index, row in data[col].items():
            if row != None and pd.isna(row)==False:
                earList.append(row)
    # return earList
    return earList

# get pilot promoiton site
def getPilotCluster():
    return prd_release[BW_releaseSch][2]

# get pilt promotion date
def getPilotDate():
    return prd_release[BW_releaseSch][3]


# get PPM Statistics
# def getPpmStatistics(BW, Urg, SV):
#     # BW=getBiWeeklyData()
#     # Urg=getUrgentData()
#     # SV=getServiceData()
#     print("Jira Number: ", getJiraNumber(BW)+getJiraNumber(Urg)+getJiraNumber(SV))
#     print("PPM Number: ", len(BW)+len(Urg)+len(SV))
#     print("Function Involved: ", len(getCombinedFunctionList(BW,Urg,SV)))
#     print("Ear Deployment: ", len(getEarData(BW)) + len(getEarData(Urg)))
#     print("Backend Deployment: ")
#     print("Bi-Weekly Request: ", len(BW))
#     print("Urgent Request: ", len(Urg))
#     print("Service Request: ", len(SV))
#     print("PPM Test Failure/Withdrawn: ", len(getFallbackData(BW,"PPM")) + len(getFallbackData(Urg,"PPM")) + len(getFallbackData(SV,"PPM")) )
#     print("AAT Test Failure: ", len(getFallbackData(BW,"AAT")) + len(getFallbackData(Urg,"AAT")) + len(getFallbackData(SV,"AAT")) )
#     print("PPS Test Failure: ", len(getFallbackData(BW,"PPS")) + len(getFallbackData(Urg,"PPS")) + len(getFallbackData(SV,"PPS")) )
#     print("PRD Test Failure: ", len(getFallbackData(BW,"PRD")) + len(getFallbackData(Urg,"PRD")) + len(getFallbackData(SV,"PRD")) )
#     print("Pilot Cluster: ", getPilotCluster())
#     print("Pilot Promotion Date: ", getPilotDate())
#     print("==================================================================================================================")
#     print("Fallback PPM Promotion", getFallbackData(BW,"PPM"), getFallbackData(Urg,"PPM"), getFallbackData(SV,"PPM"))
#     print("==================================================================================================================")
#     print("Fallback AAT Promotion", getFallbackData(BW,"AAT"), getFallbackData(Urg,"AAT"), getFallbackData(SV,"AAT"))
#     print("==================================================================================================================")
#     print("Fallback PPS Promotion", getFallbackData(BW,"PPS"), getFallbackData(Urg,"PPS"), getFallbackData(SV,"PPS"))
#     print("==================================================================================================================")
#     print("Fallback PRD Promotion", getFallbackData(BW,"PRD"), getFallbackData(Urg,"PRD"), getFallbackData(SV,"PRD"))
#     print("==================================================================================================================")


# get PPM Statistics
def getPpmStatistics(BW, Urg, SV):

    jiraNumber=(getJiraNumber(BW)+getJiraNumber(Urg)+getJiraNumber(SV))
    ppm_number=(len(BW)+len(Urg)+len(SV))
    function_involved=(len(getCombinedFunctionList(BW,Urg,SV)))
    ear_deployment=(len(getEarData(BW)) + len(getEarData(Urg)))
    # backend=("Backend Deployment: ")
    bi_weekly_request=(len(BW))
    urgent_request=(len(Urg))
    service_request=(len(SV))
    ppm_fallback=(len(getFallbackData(BW,"PPM")) + len(getFallbackData(Urg,"PPM")) + len(getFallbackData(SV,"PPM")) )
    aat_fallback=(len(getFallbackData(BW,"AAT")) + len(getFallbackData(Urg,"AAT")) + len(getFallbackData(SV,"AAT")) )
    pps_fallback=(len(getFallbackData(BW,"PPS")) + len(getFallbackData(Urg,"PPS")) + len(getFallbackData(SV,"PPS")) )
    prd_fallback=(len(getFallbackData(BW,"PRD")) + len(getFallbackData(Urg,"PRD")) + len(getFallbackData(SV,"PRD")) )
    pilot_cluster=(getPilotCluster())
    pilot_date=(getPilotDate())
    sep_line="=================================================================================================================="
    ppm_fallback_promotion=(getFallbackData(BW,"PPM"), getFallbackData(Urg,"PPM"), getFallbackData(SV,"PPM"))
    # print("==================================================================================================================")
    aat_fallback_promotion=(getFallbackData(BW,"AAT"), getFallbackData(Urg,"AAT"), getFallbackData(SV,"AAT"))
    # print("==================================================================================================================")
    pps_fallback_promotion=(getFallbackData(BW,"PPS"), getFallbackData(Urg,"PPS"), getFallbackData(SV,"PPS"))
    # print("==================================================================================================================")
    prd_fallback_promotion=(getFallbackData(BW,"PRD"), getFallbackData(Urg,"PRD"), getFallbackData(SV,"PRD"))
    # print("==================================================================================================================")

    if not os.path.isdir("{}".format(BW_releaseSch)):
        os.mkdir("{}".format(BW_releaseSch))

    with open(os.path.join("{}".format(BW_releaseSch),"result-{}.csv".format(BW_releaseSch)), mode="w",encoding="utf8") as file: # Open a file
        # jiraNumber=jiraNumber.to_string()
        # ppm_number=ppm_number.to_string()
        # function_involved=function_involved.to_string()
        # ear_deployment=ear_deployment.to_string()
        # backend=backend.to_string()
        # bi_weekly_request=bi_weekly_request.to_string()
        # urgent_request=urgent_request.to_string()
        # service_request=service_request.to_string()
        # ppm_fallback=ppm_fallback.to_string()
        # aat_fallback=aat_fallback.to_string()
        # pps_fallback=pps_fallback.to_string()
        # prd_fallback=prd_fallback.to_string()
        # pilot_cluster=pilot_cluster.to_string()
        # pilot_date=pilot_date.to_string()
        # sep_line=sep_line.to_string()
        # ppm_fallback_promotion=ppm_fallback_promotion.to_string()
        # aat_fallback_promotion=aat_fallback_promotion.to_string()
        # pps_fallback_promotion=pps_fallback_promotion.to_string()
        # prd_fallback_promotion=prd_fallback_promotion.to_string()

        file.write("Jira Number: "+str(jiraNumber))
        file.write("\n"+"PPM Number: "+str(ppm_number))
        file.write("\n"+"Function Involved: "+str(function_involved))
        file.write("\n"+"Ear Deployment: "+str(ear_deployment))
        file.write("\n"+"Backend Deployment: ")
        file.write("\n"+"Bi-Weekly Request: "+ str(bi_weekly_request))
        file.write("\n"+"Urgent Request: "+str(urgent_request))
        file.write("\n"+"Service Request: "+str(service_request))
        file.write("\n"+"PPM Revision Count: ")
        file.write("\n"+"PPM Test Failure/Withdrawn: "+str(ppm_fallback))
        file.write("\n"+"AAT Test Failure: "+str(aat_fallback))
        file.write("\n"+"PPS Test Failure: "+str(pps_fallback))
        file.write("\n"+"PRD Test Failure: "+str(prd_fallback))
        file.write("\n"+"Pilot Cluster: "+pilot_cluster)
        file.write("\n"+"Pilot Promotion Date: "+ str(pilot_date))
        file.write("\n"+sep_line)
        file.write("\n"+"Fallback PPM Promotion"+str(ppm_fallback_promotion))
        file.write("\n"+sep_line)
        file.write("\n"+"Fallback AAT Promotion"+str(aat_fallback_promotion))
        file.write("\n"+sep_line)
        file.write("\n"+"Fallback PPS Promotion"+str(pps_fallback_promotion))
        file.write("\n"+sep_line)
        file.write("\n"+"Fallback PRD Promotion"+str(prd_fallback_promotion))

        # BW_data=BW.to_string()
        # Urg_data=Urg.to_string()
        # SV_data=SV.to_string()
        # file.write(BW_data)
        # file.write(Urg_data)
        # file.write(SV_data)



def writeBackup(BW,Urg,SV):
    if not os.path.isdir("{}".format(BW_releaseSch)):
        os.mkdir("{}".format(BW_releaseSch))

    with open(os.path.join("{}".format(BW_releaseSch),"data-{}.csv".format(BW_releaseSch)), mode="w",encoding="utf8") as file: # Open a file
        BW_data=BW.to_string()
        Urg_data=Urg.to_string()
        SV_data=SV.to_string()
        file.write(BW_data)
        file.write(Urg_data)
        file.write(SV_data)

    # with open(os.path.join("{}".format(BW_releaseSch),"BW-{}.csv".format(BW_releaseSch)), mode="w",encoding="utf8") as file: # Open a file
    #     data=BW.to_string()
    #     file.write(data)

    # with open(os.path.join("{}".format(BW_releaseSch),"Urg-{}.csv".format(BW_releaseSch)), mode="w",encoding="utf8") as file: # Open a file
    #     data=Urg.to_string()
    #     file.write(data)

    # with open(os.path.join("{}".format(BW_releaseSch),"SV-{}.csv".format(BW_releaseSch)), mode="w",encoding="utf8") as file: # Open a file
    #     data=SV.to_string()
    #     file.write(data)



# with open("data.csv", mode="w",encoding="utf8") as file: # Open a file
#     data=bi_weekly["Ready for Promotion"].to_string()
#     file.write(data)



# Testing call function
# data=getUrgentData()
# print(getEarNumber(data))

# Testing String
# print(bi_weekly["Ready for Promotion"])
# for result in bi_weekly["Ready for Promotion"]:
#     if type(result) is string_:
#         print(result)

# Ouput to date.txt
# with open("data.txt", mode="w",encoding="utf8") as file: # Open a file
#     data=data.to_string()
#     file.write(data)










