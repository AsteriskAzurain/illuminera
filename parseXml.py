from xml.dom.minidom import parse

import os
# print(os.getcwd())

dom=parse('IPOFFICESD_Users.xml')
data=dom.documentElement
users=data.getElementsByTagName('tns:user')

from pandas import DataFrame
import pandas as pd

df=pd.DataFrame(columns=["loginName","E_Name","C_Name","extension"])

for user in users:
    loginname=user.getElementsByTagName('loginName')[0].childNodes[0].nodeValue.strip("@user")
    ls_name=loginname.split(' ')
    extension=user.getElementsByTagName('csm:extension')[0].childNodes[0].nodeValue
    ename=ls_name[0]
    cname=""
    if(len(ls_name)>2):
        ename=ls_name[0]+" "+ls_name[1]
        cname=ls_name[-1]
    userdict={'loginName':loginname,'E_Name':ename,'C_Name':cname,'extension':extension}
    df=df.append(userdict,ignore_index=True)
    # print(userdict)

datalength=len(users)

import datetime
now=datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
filename=str(datalength)+"_"+now+".xlsx"

df.to_excel("excel\\"+filename)