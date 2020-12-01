import os
import shutil
import sys

convertToolPath=u"D:\\3D Objects\\GitHome\\illuminera\\tool\pdf2swf.exe"
PDFsourcedir="D:\pdf2swf\srcFile"
SWFtargetdir="D:\pdf2swf\SWF"

ls_swf_id=[]
ls_except=[]
swfpath=r"\\192.168.1.245\KMSDocument\KMSSwf"
for pdffile in os.listdir(swfpath):
    pdffile_path=os.path.join(swfpath,pdffile)
    if(os.path.isfile(pdffile_path) and 'pdf' in pdffile):
        fileID=pdffile.rstrip(".pdf")
        swf_fn=fileID+".swf"
        swffile_path=os.path.join(swfpath,swf_fn)
        if(int(fileID)<=30167 and not os.path.exists(swffile_path)):
            ls_swf_id.append(fileID)
            PDFsourcePath=os.path.join(PDFsourcedir,pdffile)
            SWFtargetPath=os.path.join(SWFtargetdir,swf_fn)
            # print(pdffile_path,PDFsourcePath)
            # try:
            #     shutil.copyfile(pdffile_path, PDFsourcePath)
            # except:
            #     ls_except.append(fileID)
            # SWFtargetPath=os.path.join(SWFtargetdir,swf_fn)
            # input=('"{0}" "{1}" -o "{2}" -t '.format(convertToolPath, PDFsourcePath, SWFtargetPath))
            try:
                input=('"{0}" "{1}" -o "{2}" -t '.format(
                    convertToolPath, 
                    shutil.copyfile(pdffile_path, PDFsourcePath), 
                    SWFtargetPath)
                )
                f=open("cmdop.txt","a+")
                print(fileID,file=f)
                print(input,file=f)  
                res = os.popen(input)
                output_str = res.read()
                print(output_str,file=f)
                f.close()
            except:
                ls_except.append(fileID)
            # break

f_dst = open(r"output.txt", 'w+',encoding="utf-8")
print(',\n'.join(ls_swf_id),file=f_dst)
f_dst.close()

ls_op=[]
fop=open("cmdop.txt","r")
for line in fop:
    if (line[:5].isdigit()):
        ls_op.append(line)
    elif ("ERROR" in line):
        ls_op.append(line)
    else:
        pass
fop.close()
fnew=open("op_new.txt","w")
print(''.join(ls_op),file=fnew)
fnew.close()

fnew=open("op_new.txt","r")
fnewnew=open("op_new_new.txt","a+")
linearr=fnew.readlines()
len(linearr)
# 21740
for i in range(len(linearr)):
    line=linearr[i]     
    if("ERROR" in line and "This" in line):
        print(linearr[i-2],linearr[i],file=fnewnew)
fnewnew.close()