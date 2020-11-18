import os
import xlrd
import xlwt

written=input("评分者：")
print("需要读入的文件夹(完整路径)，如：D:/Nora 20份")
path=input("完整路径：")
os.path.normpath(path)
bookname="评分表-"+written
bookname=bookname if input("生成的表格名为【%s】，确认?(y/n)"%bookname)=="y" else input("生成的表格名称：")

workbook = xlwt.Workbook(encoding='utf-8')       #新建工作簿
sheet1 = workbook.add_sheet("Sheet1")          #新建sheet
workbook.save(r'.\%s.xls'%bookname)   #保存
sheet1.write(0,0,"No.")
sheet1.write(0,1,"Name") # 1行2列
sheet1.write(0,2,"Logic")
sheet1.write(0,3,"Written test")

index=1

for lists in os.listdir(path):
    sub_path = os.path.join(path, lists)
    if os.path.isfile(sub_path):
        filename=lists
        namearr=lists.split('.')[0].split('-')
        name=namearr[0]
        sheet1.write(index,0,str(index))
        sheet1.write(index,1,name)
        sheet1.write(index,3,written)
        index+=1

workbook.save(r'.\%s.xls'%bookname)

bookname=bookname+".xls"
print("表格【%s】已成功生成，存于【%s】。"%(bookname,os.path.abspath(bookname)))
