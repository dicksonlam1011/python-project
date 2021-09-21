import win32com.client
import pandas as pd

# HA Source Path
project_path="//dc7shdns02b/CSC1/TEAMFOLDER/PPM/Statistics_and_minutes/PPM_Statistics/2021"
project_source_path="//dc7shdns02b/CSC1/TEAMFOLDER/PPM/Statistics_and_minutes/PPM_Statistics/2021/source"
# Specify the Summary Year
summary_year=input("Enter the summary year in YYYY format: ")
# Get sample source from local file
ppm_summary = pd.ExcelFile('{}/promotion_summary_{}_Backup.xls'.format(project_source_path, summary_year))
### Part 2: Specify the Sheet Tab

promotion_type=input("Please enter the Promotion Type (01:BW, 02:Urg, 03:SV): ")
if promotion_type == "1":
    promotion_type=="Bi-weekly"
    bi_weekly=pd.read_excel(ppm_summary, 'Bi-weekly')
elif promotion_type == "2":
    promotion_type=="Urgent"
    urgent = pd.read_excel(ppm_summary, 'Urgent')
elif promotion_type == "3":
    promotion_type=="Service"
    service = pd.read_excel(ppm_summary, 'Service')


promotion_num=input("Please enter the Promotion Number (eg 2021-U0125): ")
print(bi_weekly)


###############################################################################################################



# # initiate the outlook application
# outlook = win32com.client.Dispatch('outlook.application')

# # create an email object
# mail = outlook.CreateItem(0)

# # define email information
# mail.To = 'LLM234@ha.org.hk'
# mail.Subject = "[draft] CMS {} Release for {} - AAT".format(promotion_type, promotion_num)

# with open('C:/Users/llm234/Desktop/Development-Workplace/python-project/PPM_Release_Email/html_source/draft-release-email.html', 'r', encoding="utf-8") as myfile:
#     # data=myfile.read().format(var1="test_var")
#     data=myfile.read()
# mail.HTMLBody = data

# # mail.HTMLBody = 'C:/Users/llm234/Desktop/Development-Workplace/python-project/PPM_Release_Email/html_source/draft-release-email.html'
# # mail.Body = "Testing Body"
# # mail.Attachments.Add('c:\\sample.xlsx')
# # mail.Attachments.Add('c:\\sample2.xlsx')
# # mail.CC = 'somebody@company.com'

# # Send the email
# mail.Send()