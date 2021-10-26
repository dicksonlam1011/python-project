import win32com.client
import pandas as pd
import os

# Specify the Summary Year
summary_year=input("Enter the summary year in YYYY format: ")
# Promotion Summary Path
project_source_path="//dc7shdns02b/CSC1/TEAMFOLDER/PPM/Statistics_and_minutes/PPM_Statistics/{}/source".format(summary_year)
# Get sample source from local file
ppm_summary = pd.ExcelFile('{}/promotion_summary_{}_Backup.xls'.format(project_source_path, summary_year))

### Part 2: Specify the Sheet Tab
promotion_type=input("Please enter the Promotion Type (1:BW, 2:Urg, 3:SV): ")
PPM_num=input("Please enter the Promotion Number (eg PPM2021_S0125): ")

if promotion_type == "1":
    promotion_type=="Bi-weekly"
    bi_weekly=pd.read_excel(ppm_summary, 'Bi-weekly')
    condition=bi_weekly["Serial no."]==PPM_num
    target_date=bi_weekly[condition]["Target Date"].item()
    description=bi_weekly[condition]["Description"].item()
    attachment=bi_weekly[condition]["Attachment"].item()
    eap_attachment=bi_weekly[condition]["EAP Attachment/EAP included? (Y/N)"].item()
    remarks=bi_weekly[condition]["Remarks"].item()
    acknowledgement=bi_weekly[condition]["Acknowledgement"].item()
elif promotion_type == "2":
    promotion_type=="Urgent"
    urgent = pd.read_excel(ppm_summary, 'Urgent')
    condition=urgent["Serial no."]==PPM_num
    target_date=urgent[condition]["Target Date"].item()
    description=urgent[condition]["Description"].item()
    attachment=urgent[condition]["Attachment"].item()
    eap_attachment=urgent[condition]["EAP Attachment/EAP included? (Y/N)"].item()
    remarks=urgent[condition]["Remarks"].item()
    acknowledgement=urgent[condition]["Acknowledgement"].item()
elif promotion_type == "3":
    promotion_type="Service"
    service = pd.read_excel(ppm_summary, 'Service')
    condition=service["Serial no."]==PPM_num
    target_date=service[condition]["Target Date"].item()
    description=service[condition]["Description"].item()
    attachment=service[condition]["Attachment"].item()
    eap_attachment=service[condition]["EAP Attachment/EAP included? (Y/N)"].item()
    remarks=service[condition]["Remarks"].item()
    acknowledgement=service[condition]["Acknowledgement"].item()
else:
    print("Error!!! No such promotion type!")

# Check if the promotion includes EAP
if pd.isna(eap_attachment):
    eap_promotion="NIL"
    include_eap=""
    eap_statement=""
    mail_list="LLM234@ha.org.hk"
    mail_list_cc="LLM234@ha.org.hk_No_EAP; LLM234@ha.org.hk_No_EAP"
else:
    eap_promotion="Please refer to E-form for details"
    include_eap="including WebLogic Promotion"
    eap_statement="For those requests involve EAP promotion, IMPs should schedule rollout to hospitals after EAP promotion complete"
    mail_list="LLM234@ha.org.hk"
    mail_list_cc="LLM234@ha.org.hk_EAP; LLM234@ha.org.hk_EAP"

# Check if Remarks are empty
if pd.isna(remarks):
    remarks=" "
else:
    remarks=remarks.split("/ ")
    #print(remarks)


if pd.isna(acknowledgement):
    acknowledgement_summary=" "
else:
    with open('C:/Users/llm234/Desktop/Development-Workplace/python-project/PPM_Release_Email/html_source/acknowledgement_summary.html', 'r', encoding="utf-8") as myfile:
        acknowledgement_summary=myfile.read().format(PPM_Number=PPM_num,Acknowledgement=acknowledgement)
        #acknowledgement="HTML"

###############################################################################################################


def draftPRDemail(mail_list, mail_list_cc):
    # initiate the outlook application
    outlook = win32com.client.Dispatch('outlook.application')
    # create an email object
    mail = outlook.CreateItem(0)
    # define email information
    mail.To = mail_list
    mail.CC = mail_list_cc
    mail.Subject = "CMS {} Release for {}".format(promotion_type, PPM_num)
    # Write Email Body
    with open('C:/Users/llm234/Desktop/Development-Workplace/python-project/PPM_Release_Email/html_source/draft-K2-form-email.html', 'r', encoding="utf-8") as myfile:
        data=myfile.read().format(PPM_Number=PPM_num, Description=description, Target_date=target_date, Attachment=attachment, year=summary_year, Acknowledgement_Summary=acknowledgement_summary, EAP_Promotion=eap_promotion, Include_EAP=include_eap, EAP_Statement=eap_statement, Remarks=remarks)
    mail.HTMLBody = data
    #Save the PRD email to specific path
    mail.SaveAs("//dc7shdns02b/CSC1/TEAMFOLDER/PPM/Statistics_and_minutes/DailyTask/Dickson/Backup/TEMP-draft-email-backup/{}.msg".format(mail.Subject))

def draftEmail():
    draftPRDemail(mail_list, mail_list_cc)
    # initiate the outlook application
    outlook = win32com.client.Dispatch('outlook.application')
    # create an email object
    mail = outlook.CreateItem(0)
    # define email information
    mail.To = 'LLM234@ha.org.hk'
    #mail.CC = 'HO IT&HI CMS PPM Support <haitscmsppmsupt@ho.ha.org.hk>; Gary FUNG, HOIT&HI CJP(CRC2)1 <FKH688@ha.org.hk>'
    mail.Subject = "[draft] CMS {} Release for {} -AAT".format(promotion_type, PPM_num)
    # Write Email Body
    with open('C:/Users/llm234/Desktop/Development-Workplace/python-project/PPM_Release_Email/html_source/draft-K2-form-email.html', 'r', encoding="utf-8") as myfile:
        data=myfile.read().format(PPM_Number=PPM_num, Description=description, Target_date=target_date, Attachment=attachment, year=summary_year, Acknowledgement_Summary=acknowledgement_summary, EAP_Promotion=eap_promotion, Include_EAP=include_eap, EAP_Statement=eap_statement, Remarks=remarks)
    mail.HTMLBody = data
    PRD_email="CMS {} Release for {}.msg".format(promotion_type, PPM_num)
    mail.Attachments.Add('//dc7shdns02b/CSC1/TEAMFOLDER/PPM/Statistics_and_minutes/DailyTask/Dickson/Backup/TEMP-draft-email-backup/{}'.format(PRD_email))
    # Send out the email
    mail.Send()
    print("Send out draft email for {}".format(PPM_num))


# draftEmail()
print(description)



########## Reference only #################################
# mail.HTMLBody = 'C:/Users/llm234/Desktop/Development-Workplace/python-project/PPM_Release_Email/html_source/draft-release-email.html'
# mail.Body = "Testing Body"
# mail.Attachments.Add('c:\\sample.xlsx')
# mail.Attachments.Add('c:\\sample2.xlsx')
# mail.CC = 'somebody@company.com'

# Send the email
# mail.Send()

# Save the email to draft box
# mail.Save()
