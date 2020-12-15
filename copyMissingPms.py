# -*- coding:utf-8 -*-
# copy  "\\192.168.1.245\KMSDocument\KMSSwf\print2flash" t1_Id.xml + t1_Id_files
# to    "\\192.168.1.245\Project SWF" t2_sqlFileID.xml + t2_sqlFileID_files
import os
from os import path
import shutil
import pandas as pd

data_path = r"D:\BingWei\OneDrive - stu.sbs.edu.cn\illuminera\Desktop\missingPMS.xlsx"

data = pd.read_excel(io=data_path, header=0)
# print(data.columns.values)
# ['t1_title' 't1_Id' 't1_srcTable' 't1_sqlID' 't1_status' 't2_Id' 't2_srcTable' 't2_status' 't2_sqlID' 't2_sqlFileID']

# print(data.head())
#                                             t1_title  t1_Id  t1_srcTable  t1_sqlID  t1_status  t2_Id  t2_srcTable  t2_status  t2_sqlID                          t2_sqlFileID
# 0  #1. PNS NPD (Idea generation and initial conce...   4452            0     54057          1   6204            1          2      1907  0ADAA7DC-7C06-43EF-AF7D-10501F235842
# 1                           #2.PMF summary FINAL.ppt   4458            0     54063          1   6205            1          2      1908  643669D3-7801-4482-AD3D-138973266F17
# 2                #3. Gold Baby Club Report FINAL.ppt   4460            0     54065          1   6206            1          2      1909  62C14BAA-6A15-4DE6-A6C2-CC84E93C6FFB
# 3        #6. Quick Response Pricing - Lema Space.ppt   4462            0     54067          1   6208            1          2      1911  3C068D23-2571-47AD-8725-2440D977BE63
# 4  #9. Super Premium IMF Full Report 22FEB 2012 F...   4464            0     54069          1   6209            1          2      1912  0973428D-A736-4FE2-8297-AD52887B1ABF

srcpath = r"\\192.168.1.245\KMSDocument\KMSSwf\print2flash"
tgtpath = r"\\192.168.1.245\Project SWF"

ls_update=[]
updatesql="update t_Jobs_P2FConvertRecord set status=1 where srcTable=1 and sqlID in({})"

for item in data.itertuples():
    srcfn = str(getattr(item, 't1_sqlID'))
    tgtfn = getattr(item, 't2_sqlFileID')
    if getattr(item, 't1_status') == 1 and getattr(item, 't2_status') != 1 and not pd.isnull(tgtfn):
        ls_update.append(str(getattr(item,'t2_sqlID')))
        p1=os.path.join(srcpath, srcfn)
        p2=os.path.join(tgtpath,tgtfn)
        if os.path.exists(p1+".xml") and os.path.exists(p1+"_files"):
            shutil.copyfile(p1+".xml",p2+".xml")
            shutil.copytree(p1+"_files",p2+"_files")

f_dst = open(r"output.txt", 'w+',encoding="utf-8")
print(updatesql.format(','.join(ls_update)),file=f_dst)
f_dst.close()