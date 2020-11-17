from pandas import DataFrame
import pandas as pd

import os

df=pd.DataFrame(columns=["连续","分机号","英文名","中文名","loginName","备注"])

cardfile='card0818.xlsx'
cardinfo=pd.read_excel(io=cardfile,header=0)
extfile='excel\\systemData.xlsx'
extdata=pd.read_excel(io=extfile,header=0)

# print(len(cardinfo))
# print(cardinfo.columns.values)
# print(len(extdata))
# print(extdata.columns.values)

remark=ename=cname=loginName=extension=sy_ename=""
    # 1. 根据ext匹配data里的数据
    # 2. 填入ename cname loginname 
    # 3. loginname: 'Switchboard'->前台
    #               ['Hugo','Bacon','Mozart','Goeth','Copernic','Haydn']->电话间
    #               ['Newton','Einstein','Galileo','Franklin','Da Vinci']->会议室
ls_r1=['Newton','Einstein','Galileo','Franklin','Da Vinci']
ls_r2=['Hugo','Bacon','Mozart','Goeth','Copernic','Haydn']

for index in range(200):
    indexEXT=8000+index
    for i in range(len(extdata)):
        sy_ext=int(extdata['extension'][i])
        if(sy_ext==indexEXT):
            loginName=str(extdata['loginName'][i]).strip()
            if loginName in ls_r1:
                remark="会议室 "
            elif loginName in ls_r2:
                remark="电话间 "
            else:
                remark="前台 " if(loginName=="Switchboard ") else ''
            sy_cname=loginName.split(' ')[-1]
            sy_ename=loginName.strip(sy_cname)
            break
    for j in range(len(cardinfo)):
        card_ext=int(cardinfo['分机号'][j])
        if(card_ext==indexEXT):
            ename=str(cardinfo['英文名'][j]).strip()
            cname=str(cardinfo['中文名'][j]).strip()
            if(sy_ename!="" and ename!=sy_ename.strip()):
                print(sy_ename+'\t'+ename)
                remark+="缩写"
            break
    if(sy_ext==card_ext):
        extension=sy_ext
    if(loginName==''):
        remark="留空 "
    userdict={'连续':indexEXT,'分机号':extension,'英文名':ename,'中文名':cname,'loginName':loginName,'备注':remark}
    df=df.append(userdict,ignore_index=True)
    remark=ename=cname=loginName=extension=sy_ename=""

import datetime
now=datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
filename="分机号_"+now+".xlsx"

df.to_excel("分机号归档\\"+filename)
