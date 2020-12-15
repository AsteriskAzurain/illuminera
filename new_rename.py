# rename folders&xmlfiles in fatherdir
# folder: xxx.ext_files -> xxx_files
# xml: xxx.ext.xml -> xxx.xml

import os, datetime

print("renamed start:\t"+datetime.datetime.today().strftime('%Y-%m-%d'))

fatherdir=r"D:\CopyandConvert\batch_result"
tgtdir=r"D:\CopyandConvert\renamed_result"

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

import shutil

srcfile=r"D:\3D Objects\code bak\ERP\articleView\docviewer.html"
tgtfile=r"\\192.168.1.245\Project SWF\docviewer.html"
shutil.copyfile(src=srcfile,dst=tgtfile)