import PPM_Summary_excel as summary

BW=summary.getBiWeeklyData()
Urg=summary.getUrgentData()
SV=summary.getServiceData()

summary.getPpmStatistics(BW,Urg,SV)
summary.writeBackup(BW,Urg,SV)
summary.getFunctionDataToImage(BW,Urg,SV)

