import os
import pandas as pd
import numpy as np
import shutil

# "D:\BingWei\OneDrive - stu.sbs.edu.cn\illuminera\print2flash\missing\kms"
# "D:\BingWei\OneDrive - stu.sbs.edu.cn\illuminera\print2flash\missing\pms"

tgt_kms_path = r"D:\BingWei\OneDrive - stu.sbs.edu.cn\illuminera\print2flash\missing\kms"
tgt_pms_path = r"D:\BingWei\OneDrive - stu.sbs.edu.cn\illuminera\print2flash\missing\pms"

# "D:\BingWei\OneDrive - stu.sbs.edu.cn\illuminera\print2flash\missing\kms_20201118_124231.xlsx"
# "D:\BingWei\OneDrive - stu.sbs.edu.cn\illuminera\print2flash\missing\pms_20201118_113922.xlsx"
kmsFile = r"D:\BingWei\OneDrive - stu.sbs.edu.cn\illuminera\print2flash\missing\kms_20201118_124231.xlsx"
pmsFile = r"D:\BingWei\OneDrive - stu.sbs.edu.cn\illuminera\print2flash\missing\pms_20201118_113922.xlsx"

kmsData = pd.read_excel(io=kmsFile, header=0, index_col='Id')
pmsData = pd.read_excel(io=pmsFile, header=0,
                        index_col='Id', usecols=[1, 3, 4, 5, 6, 7])
print(kmsData.columns.values, '\n', pmsData.columns.values)
print(kmsData[:3], pmsData[:3])

# kms
ls_kms_else = []
ls_kms_except = []
for ki, krow in kmsData.iterrows():
    sql_id = ki
    status = krow['status']
    filetype = str(krow['Title']).split('.')[-1]
    filepath = krow['ArticleLink']
    if os.path.isfile(filepath):
        kname = str(sql_id)+"."+filetype
        newname = os.path.join(tgt_kms_path, kname)
        try:
            shutil.copyfile(filepath, newname)
        except:
            ls_kms_except.append(sql_id)
    else:
        ls_kms_else.append(sql_id)
        print("id:{0},\t,status:{1}".format(sql_id, status))

print(len(ls_kms_else), '\t', len(ls_kms_except))

for id in ls_kms_else:
    print(kmsData['status'][int(id)])

# output:
#   len(ls_kms_else)=17
#   status: all'Fail and Copy Failed'


# pms
ls_pms_else = []
ls_pms_except = []
for pi, prow in pmsData.iterrows():
    sql_id = pi
    status = prow['status']
    if not("exist" in status):
        filename = str(prow['FileID']).strip()
        filetype = str(prow['FileNameType']).strip()
        filepath = str(prow['FileFolder']).replace("E:", r"\\192.168.1.245")
        filepath = os.path.join(filepath, prow['FileName'])
        # print(pi,filepath)
        if os.path.isfile(filepath):
            pname = filename+"."+filetype
            newname = os.path.join(tgt_pms_path, pname)
            # print('\t',pname,newname)
            try:
                shutil.copyfile(filepath, newname)
            except:
                ls_pms_except.append(sql_id)
        else:
            ls_pms_else.append(sql_id)
            print("id:{0},\tstatus:{1}".format(sql_id, status))

print(len(ls_pms_else), '\t', len(ls_pms_except))

# output:
#   len(ls_kms_else)=1
#   id:13927, status:/

# D:\BingWei\OneDrive - stu.sbs.edu.cn\illuminera\print2flash\missing\kms_flash
# D:\BingWei\OneDrive - stu.sbs.edu.cn\illuminera\print2flash\missing\pms_flash
# D:\BingWei\OneDrive - stu.sbs.edu.cn\illuminera\print2flash\missing\flash\kms
# D:\BingWei\OneDrive - stu.sbs.edu.cn\illuminera\print2flash\missing\flash\pms
src_kms_path = r"D:\BingWei\OneDrive - stu.sbs.edu.cn\illuminera\print2flash\missing\kms_flash"
src_pms_path = r"D:\BingWei\OneDrive - stu.sbs.edu.cn\illuminera\print2flash\missing\pms_flash"
tgt_flash_kms = r"D:\BingWei\OneDrive - stu.sbs.edu.cn\illuminera\print2flash\missing\flash\kms"
tgt_flash_pms = r"D:\BingWei\OneDrive - stu.sbs.edu.cn\illuminera\print2flash\missing\flash\pms"

# kms
ls_kms_rnfail_f = []
ls_kms_rnfail_d = []
for kfile in os.listdir(src_kms_path):
    kpath = os.path.join(src_kms_path, kfile)
    kid = kfile[:5]
    if(os.path.isfile(kpath) and 'xml' in kfile):
        knewname = kid+".xml"
        # print(kpath,os.path.join(tgt_flash_kms,knewname))
        try:
            os.rename(kpath, os.path.join(tgt_flash_kms, knewname))
        except:
            print("id:\t"+kid)
            ls_kms_rnfail_f.append(kid)
    elif(os.path.isdir(kpath) and "_files" in kpath):
        knewname = kid+"_files"
        # print(kpath,os.path.join(tgt_flash_kms,knewname))
        try:
            os.rename(kpath, os.path.join(tgt_flash_kms, knewname))
        except:
            print("id:\t"+kid)
            ls_kms_rnfail_d.append(kid)
    else:
        pass
print(len(ls_kms_rnfail_f), len(ls_kms_rnfail_d))

# pms
ls_pms_rnfail_f = []
ls_pms_rnfail_d = []
for pfile in os.listdir(src_pms_path):
    ppath = os.path.join(src_pms_path, pfile)
    # pid=pfile[:36]
    pid = pfile.split('.')[0]
    print(pid)
    if(os.path.isfile(ppath) and 'xml' in pfile):
        pnewname = pid+".xml"
        # print(ppath,os.path.join(tgt_flash_pms,pnewname))
        try:
            os.rename(ppath, os.path.join(tgt_flash_pms, pnewname))
        except:
            print("id:\t"+pid)
            ls_pms_rnfail_f.append(pid)
    elif(os.path.isdir(ppath) and "_files" in ppath):
        pnewname = pid+"_files"
        # print(ppath,os.path.join(tgt_flash_pms,pnewname))
        try:
            os.rename(ppath, os.path.join(tgt_flash_pms, pnewname))
        except:
            print("id:\t"+pid)
            ls_pms_rnfail_d.append(pid)
    else:
        pass
print(len(ls_pms_rnfail_f), len(ls_pms_rnfail_d))

# kms
kms_father_path = r"D:\BingWei\OneDrive - stu.sbs.edu.cn\illuminera\print2flash\missing\kms_flash"
kms_tgt_path = r"D:\BingWei\OneDrive - stu.sbs.edu.cn\illuminera\print2flash\missing\flash\kms_renamed"
for fatherdir in os.listdir(kms_father_path):
    flash_path = os.path.join(kms_father_path, fatherdir)
    sql_id = str(fatherdir[:5])
    if (os.path.isdir(flash_path) and sql_id.isdigit()):
        for flashfile in os.listdir(flash_path):
            innerpath = os.path.join(flash_path, flashfile)
            if(os.path.isdir(innerpath) and '_files' in flashfile):
                new_dir_name = os.path.join(kms_tgt_path, sql_id+"_files")
                # print(innerpath+'\n'+new_dir_name)
                os.rename(innerpath, new_dir_name)
            elif (os.path.isfile(innerpath) and 'xml' in flashfile):
                new_xml_name = os.path.join(kms_tgt_path, sql_id+".xml")
                # print(innerpath+'\n'+new_xml_name)
                os.rename(innerpath, new_xml_name)
            else:
                pass

# pms
pms_father_path=r"D:\BingWei\OneDrive - stu.sbs.edu.cn\illuminera\print2flash\missing\pms_flash"
pms_tgt_path=r"D:\BingWei\OneDrive - stu.sbs.edu.cn\illuminera\print2flash\missing\flash\pms_renamed"
for fatherdir_1 in os.listdir(pms_father_path):
    flash_path_1=os.path.join(pms_father_path,fatherdir_1)
    for flashfile_1 in os.listdir(flash_path_1):
        innerpath_1=os.path.join(flash_path_1,flashfile_1)
        if(os.path.isdir(innerpath_1) and '_files' in flashfile_1):
            new_dir_name_1=os.path.join(pms_tgt_path,fatherdir_1+"_files")
            # print(fatherdir_1+'\n\t'+innerpath_1+'\n\t'+new_dir_name_1)
            os.rename(innerpath_1,new_dir_name_1)
        elif (os.path.isfile(innerpath_1) and 'xml' in flashfile_1):
            new_xml_name_1=os.path.join(pms_tgt_path,fatherdir_1+".xml")
            # print(fatherdir_1+'\n\t'+innerpath_1+'\n\t'+new_xml_name_1)
            os.rename(innerpath_1,new_xml_name_1)
        else:
            pass
