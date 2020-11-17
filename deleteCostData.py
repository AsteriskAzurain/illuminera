ls_comID=[3728, 3728, 3851, 5119, 5119, 5291, 5292, 5293, 5328, 5390, 5391, 5392, 5393, 5397, 5398, 5420, 5426, 5430, 5433, 5434, 5435]

str_0="select CostingType as 'costType', * from t_PMS_ProjectCostingInfo where ComponentId={} order by 'costType';"
str_1="select Id,Rate,Type from t_PMS_ProjectCostingInfo where ComponentId={};"
ls_all_0=[]
ls_info_1=[]
for comID in ls_comID:
    ls_all_0.append(str_0.format(comID))
    ls_info_1.append(str_1.format(comID))

 for line in ls_all_0:
     print(line)
     
import pymssql
import pandas as pd

server="192.168.1.245"
user="sa"
password="Illuminera2011"
database="IllumineraERP"
conn = pymssql.connect(server, user, password, database)

cursor = conn.cursor()

ls_tup=[]
for comID in ls_comID:
    cursor.execute('select * from t_PMS_ProjectCostingInfo where ComponentId=%s order by ComponentId,CostingType',comID)
    row = cursor.fetchone()
    for row in cursor: # len(row)=17
        print(row[0],row[2],row[-3])
        ls_tup.append(row)
# while row:
#     print("ID=%d, Rate=%d, Type=%d" % (row[0], row[1], row[2]))
#     row = cursor.fetchone()

df = pd.DataFrame(ls_tup, columns =['Id','ProId','ComponentId','QCSupervisorId','DPSupervisorId','MailStatus','EmailtoFWUserId','EmailtoFWDate','FWEmailtoResearchUserId',
	'FWEmailtoResearchDate','CostingConfirmUserId','CostingConfirmDate','MethodologyTypeId','MethodologyId','CostingType','Rate','Type'])

df.to_excel("0922(3).xlsx")
# 关闭连接
conn.close()

import os
os.chdir("D:\\Desktop")