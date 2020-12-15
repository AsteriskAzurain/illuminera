import os
from typing import IO
import pandas as pd
import numpy as np

ckpms_file=r"D:\BingWei\OneDrive - stu.sbs.edu.cn\illuminera\Desktop\checkStatus.xlsx"
ckdata=pd.read_excel(io=ckpms_file,header=0)
print(ckdata.columns.values)
# ['id' 'status' 'sqlID' 'sqlFileID' 'title']

pmsswf_path=r"\\192.168.1.245\Project SWF"
update_sql="update ConvertLog set status=1 where srcTable=1 and sqlID={}"
ls_success=[]
for index,row in ckdata.iterrows():
    if os.path.exists(os.path.join(pmsswf_path,str(row['sqlFileID'])+".xml")):
        ls_success.append(row['sqlID'])
print(len(ls_success),'/',len(ckdata))

print('\n'.join([update_sql.format(id) for id in ls_success]))

kmsswf_path=r"\\192.168.1.245\KMSDocument\KMSSwf\print2flash"
update_sql_1="update ConvertLog set status=1 where srcTable=0 and sqlID in ({})"
ls_success_1=[]
for index,row in ckdata.iterrows():
    if os.path.exists(os.path.join(kmsswf_path,str(row['sqlID'])+".xml")):
        ls_success_1.append(row['sqlID'])
print(len(ls_success_1),'/',len(ckdata))

f_dst = open(r"output.txt", 'w+',encoding="utf-8")
print(update_sql_1.format(','.join('%s' %id for id in ls_success_1)),file=f_dst)
f_dst.close()