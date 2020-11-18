# "\\192.168.1.245\KMSDocument\KMSSwf\print2flash\30285_files"

import os
# os.chdir(r"\\192.168.1.245\KMSDocument\KMSSwf\print2flash")

ls_swf_id=[]
swfpath=r"\\192.168.1.245\KMSDocument\KMSSwf\print2flash"
for swffile in os.listdir(swfpath):
    swffile_path=os.path.join(swfpath,swffile)
    if(os.path.isfile(swffile_path)):
        sqlID=swffile.rstrip(".xml")
        if not(sqlID in ls_swf_id):
            ls_swf_id.append(sqlID)

print(len(ls_swf_id))

from datetime import datetime
now=datetime.now().strftime("%Y%m%d_%H%M%S")
f_dst = open(r"D:\CopyandConvert\pms_feedback_{0}.txt".format(now), 'w+',encoding="utf-8")
print(',\n'.join(ls_swf_id),file=f_dst)
f_dst.close()

otherpath=r"D:\CopyandConvert\KMSSwf"
for filename in os.listdir(otherpath):
    subpath=os.path.join(otherpath,filename)
    if(os.path.isdir(subpath) and '_files' in filename):
        fileid=filename[:5]
        old_dir_name=subpath
        new_dir_name=os.path.join(r"D:\CopyandConvert\renamedSWF",fileid+"_files")
        os.rename(old_dir_name,new_dir_name)
    elif(os.path.isfile(subpath) and 'xml' in filename):
        fileid=filename[:5]
        old_xml_name=subpath
        new_xml_name=os.path.join(r"D:\CopyandConvert\renamedSWF",fileid+".xml")
        os.rename(old_xml_name,new_xml_name)
    else:
        print(filename)

ls_swf_fileid=[]
pms_flash_path=r"\\192.168.1.245\Project SWF"
for flash_filename in os.listdir(pms_flash_path):
    pms_subpath=os.path.join(pms_flash_path,flash_filename)
    if(os.path.isfile(pms_subpath)):
        sql_fileID=flash_filename.rstrip(".xml")
        if not(sql_fileID in ls_swf_fileid):
            ls_swf_fileid.append(sql_fileID)

print(len(ls_swf_fileid))

from datetime import datetime
now=datetime.now().strftime("%Y%m%d_%H%M%S")
f_dst1 = open(r"D:\fileid.txt", 'w+',encoding="utf-8")
print(now,'\n\n',ls_swf_fileid,file=f_dst1)
f_dst1.close()

import pandas as pd
import numpy as np

sqlFile=r"D:\Documents\fileid.csv"
pmsData=pd.read_csv(sqlFile)

pmsData[:5]

pmsData.columns.values

ls_sql_fileid=pmsData['NULL'].tolist()

ls_pms_sql=[str(item).lower() for item in ls_sql_fileid]
ls_pms_flash=[item.lower() for item in ls_swf_fileid]

ls_pms_sub=list(set(ls_pms_sql).difference(set(ls_pms_flash)))

# missingPMS
ls_pms_sub1=["'"+str(item)+"'" for item in ls_pms_sub]
now=datetime.now().strftime("%Y%m%d_%H%M%S")
f_dst2 = open(r"D:\missingPMS.txt", 'w+',encoding="utf-8")
print(now,'\n\n',',\n'.join(ls_pms_sub1),file=f_dst2)
f_dst2.close()