from datetime import date
import json
import requests
from datetime import datetime

from requests.models import Response

nextyear = datetime.today().year+1

holiday_url2 = "http://timor.tech/api/holiday/year/{0}".format(nextyear)

response = requests.get(holiday_url2)
result = response.json()

dict_holidays={}
ls_holidays=[]
ls_workdays=[]
if(result["code"]==0):
    dict_hols=result["holiday"]
    for k,v in dict_hols.items():
        hol=datetime.strptime(v["date"],"%Y-%m-%d")
        if not(v["holiday"]):
            ls_workdays.append(hol)
        else:
            v["name"]=u"春节" if any(s in v["name"] for s in [u"除夕",u"初"]) else v["name"]
            dict_holidays.update({hol:v})
            ls_holidays.append(hol)

ls_holidays.sort()
dict_pkg={}
for day in ls_holidays:
    holname=dict_holidays[day]["name"] #.encode('utf-8')
    datestr=dict_pkg[holname]+"," if holname in dict_pkg.keys() else ""
    datestr+=(day.strftime("%Y-%m-%d"))
    dict_pkg[holname]=datestr
# print(dict_pkg["春节"])
#print('\n'.join([dict_holidays[key]['name'].encode('utf-8') for key in ls_holidays]))
config_val=";\n".join(dict_pkg.values())+";"
config_val2=','.join([day.strftime("%Y-%m-%d") for day in ls_workdays])+';'
print(config_val,'\n\n',config_val2)

for day,str in dict_pkg.items():
    print("{0}:\n\t{1}".format(day,str))

# 2021-01-01,2021-01-02,2021-01-03;
# 2021-02-11,2021-02-12,2021-02-13,2021-02-14,2021-02-15,2021-02-16,2021-02-17;
# 2021-04-03,2021-04-04,2021-04-05;
# 2021-05-01,2021-05-02,2021-05-03,2021-05-04,2021-05-05;
# 2021-06-12,2021-06-13,2021-06-14;
# 2021-09-19,2021-09-20,2021-09-21;
# 2021-10-01,2021-10-02,2021-10-03,2021-10-04,2021-10-05,2021-10-06,2021-10-07;
