#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :new_rename.py
@说明        :rename folders&xmlfiles in fatherdir
                folder: xxx.ext_files -> xxx_files
                xml: xxx.ext.xml -> xxx.xml
@时间        :2020/12/2 13:21:35‎
@作者        :Asterisk Fang
'''

'''
规范转换过程
1 run convert program
2 run p2f batch process app
3 rename converted files
4 copy doc.html to 245
5 copy renamed files to 245
6 copy srcFiles & flash files to onedrive
'''

import os, datetime, shutil

local_dir=r"D:\CopyandConvert"
server_dir=r"\\192.168.1.245\Project SWF"
archive_dir=r"D:\BingWei\OneDrive - stu.sbs.edu.cn\illuminera\print2flash"

today=datetime.datetime.today()
td_str="NeedtoConvert_"+today.strftime('%m%d')

print("renamed start:\t"+today.strftime('%Y-%m-%d'))

fatherdir=os.path.join(local_dir,"batch_result")
tgtdir=os.path.join(local_dir,"renamed_result")

for son in os.listdir(fatherdir):
    sql_fileID=son.split('.')[0]
    son_path=os.path.join(fatherdir,son)
    if(os.path.isdir(son_path) and "files" in son):
        new_dir_name=sql_fileID+"_files"
        os.rename(son_path,os.path.join(tgtdir,new_dir_name))
    elif(os.path.isfile(son_path) and 'xml' in son):
        new_xml_name=sql_fileID+".xml"
        os.rename(son_path,os.path.join(tgtdir,new_xml_name))
    else:
        pass
print("\nrenamed end.")

# cp .../renamed_result/* 245/Project SWF/
shutil.copytree(src=tgtdir,dst=server_dir,dirs_exist_ok=True)

doc_srcfile=r"D:\3D Objects\code bak\ERP\articleView\docviewer.html"
doc_tgtfile=os.path.join(server_dir,"docviewer.html")
shutil.copyfile(src=doc_srcfile,dst=doc_tgtfile)

# cp need2convert_xxx to onedrive
archive_tgtdir=os.path.join(archive_dir,"CopyandConvert_pms")
ls_docdir=[]
for docdir in os.listdir(local_dir):
    docpath=os.path.join(local_dir,docdir)
    if os.path.isdir(docpath) and td_str in docdir:
        ls_docdir.append(docdir)
        shutil.move(docpath,archive_tgtdir)
print(ls_docdir)

archive_flash_dir=os.path.join(archive_tgtdir,ls_docdir[0])
shutil.copytree(src=tgtdir,dst=os.path.join(archive_flash_dir,"renamed_result"))
shutil.rmtree(tgtdir)
if not os.path.exists(tgtdir):
    os.mkdir(tgtdir)