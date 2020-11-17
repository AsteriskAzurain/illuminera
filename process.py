import os
import pandas as pd

os.chdir(r"D:\CopyandConvert_pms")
os.getcwd()

sourceFile="./data_copyFailed.xlsx"
sourceData=pd.read_excel(io=sourceFile,header=0)

print(len(sourceData))
# 124
print(sourceData.columns.values)
# ['Unnamed: 0' 'sn' 'status' 'fileID' 'createTime' 'title' 'fileName' 'fileType']

import datetime
import pymssql
import pandas as pd
from shutil import copyfile

server="192.168.1.245"
user="sa"
password="Illuminera2011"
database="IllumineraERP"
conn = pymssql.connect(server, user, password, database)

cursor = conn.cursor()

ls_dst=[]
for i in range(len(sourceData)):
    sn=sourceData['sn'][i]
    status=sourceData['status'][i]
    sql_ID=sourceData['fileID'][i]
    sql="select FileID from t_PMS_UploadFileInfo where Id="+str(sql_ID)
    cursor.execute(sql)
    sql_fileID=cursor.fetchone()[0]
    # 2020/11/4 23:48:24
    createTime= datetime.datetime.strptime(sourceData['createTime'][i], '%Y/%m/%d %H:%M:%S')
    timeStr=createTime.strftime("%m%d%H")
    title=sourceData['title'][i]
    fileName=sourceData['fileName'][i]
    fileType=sourceData['fileType'][i]
    # D:\CopyandConvert_pms\sourcefile\110422
    srcPath=os.path.join(r"D:\CopyandConvert_pms\sourcefile",timeStr,title)
    dstFile=str(sql_fileID)+'.'+fileType
    # D:\CopyandConvert_pms\NeedtoConvert_110611
    dstPath=os.path.join(r"D:\CopyandConvert_pms",("NeedtoConvert_"+timeStr),dstFile)
    # print(srcPath,dstPath)
    ls_dst.append(copyfile(srcPath,dstPath))
    # break

# "D:\CopyandConvert_pms\output2.txt"
f_dst = open(r"D:\CopyandConvert_pms\output2.txt", 'w+',encoding="utf-8")
print(ls_dst,file=f_dst)
f_dst.close()

for i in range(len(sourceData)):
    sn=sourceData['sn'][i]
    status=sourceData['status'][i]
    sql_ID=sourceData['fileID'][i]
    sql="select FileID from t_PMS_UploadFileInfo where Id="+str(sql_ID)
    cursor.execute(sql)
    sql_fileID=cursor.fetchone()[0]
    createTime= datetime.datetime.strptime(sourceData['createTime'][i], '%Y/%m/%d %H:%M:%S')
    timeStr=createTime.strftime("%m%d%H")
    title=sourceData['title'][i]
    fileName=sourceData['fileName'][i]
    fileType=sourceData['fileType'][i]
    srcPath=os.path.join(r"D:\CopyandConvert_pms\sourcefile",timeStr,title)
    dstFile=str(sql_fileID)+'.'+fileType
    dstPath=os.path.join(r"D:\CopyandConvert_pms",("NeedtoConvert_110612"),dstFile)
    copyfile(srcPath,dstPath)

conn.close()