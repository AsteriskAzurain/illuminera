import os

ls_fileID=[]
flash_path=r"D:\CopyandConvert_pms\NeedtoConvert_110612\flash2"
for topfolders in os.listdir(flash_path):
    sub_path = os.path.join(flash_path, topfolders)
    if os.path.isdir(sub_path):
        fileID=topfolders.rstrip("_files")
        ls_fileID.append(fileID)
        for file in os.listdir(sub_path):
            inner_path=os.path.join(sub_path,file)
            if(os.path.isdir(inner_path)):
                old_dir_name=inner_path
                new_dir_name=os.path.join(r"D:\CopyandConvert_pms\NeedtoConvert_110612\flash3",fileID+"_files")
                # print("dir:\n\told: ",old_dir_name,"\n\tnew: ",new_dir_name)
                os.rename(old_dir_name,new_dir_name)
            elif(os.path.isfile(inner_path) and 'xml' in file):
                old_file_name=inner_path
                new_file_name=os.path.join(r"D:\CopyandConvert_pms\NeedtoConvert_110612\flash3",fileID+".xml")
                # print("xml:\n\told: ",old_file_name,"\n\tnew: ",new_file_name)
                os.rename(old_file_name,new_file_name)
            else:
                pass