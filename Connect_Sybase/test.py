import pyodbc
import datetime

serv = "cms-v2corp-st1"

usr = "sa" 

passwd = "ppmadmcorp"

db = "pat_program"

prt = "23361"

drver="Adaptive Server Enterprise"

#driver="FreeTDS"

query="select * from programme_registry where programme_code in ('RM-PPM', 'RM-CRTP', 'RM-ICD', 'RM-CRTD', 'RM-SICD', 'RM-ICM')"

print (datetime.datetime.now())

conn = pyodbc.connect(driver=drver, server=serv, database=db,port = prt,uid=usr, pwd=passwd)

print(conn)

cursor = conn.cursor()

cursor.execute(query)

rows = cursor.fetchall()

# for row in rows:
print(rows)

# print(row)

conn.close()