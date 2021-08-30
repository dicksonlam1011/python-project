import PPM_Summary_excel as summary

BW=summary.getBiWeeklyData()
Urg=summary.getUrgentData()
SV=summary.getServiceData()

summary.getPpmStatistics(BW,Urg,SV)

