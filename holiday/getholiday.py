from datetime import date
import json
import requests
from datetime import datetime

from requests.models import Response

nextyear = datetime.today().year+1

# 根据传入年份返回当年假期列表
# http://v.juhe.cn/calendar/year?year=2018&key=您申请的appKey
# key:0266532af782db82e99f7e99248abcf2
# 请求地址：http://v.juhe.cn/calendar/year
# 请求参数：year=2021&key=0266532af782db82e99f7e99248abcf2
# 请求方式：GET
# holiday_url="http://v.juhe.cn/calendar/year"
# holiday_url+="?year={0}&key=0266532af782db82e99f7e99248abcf2"
# response=requests.get(holiday_url.format(nextyear))
# result=response.json()
# print(result)
# 暂无21年数据
# {'reason': 'No data returned', 'result': None, 'error_code': 217701}

holiday_url = "http://tool.bitefu.net/jiari?d={0}".format(nextyear)

# # 0工作日 1 假日 2节日
response = requests.get(holiday_url)
result = response.json()

template='<add key="LegalHolidays{0}" value="{1}"/>'

ls_holidays=[]
for daystr in result[str(nextyear)].keys():
    holiday=datetime.strptime(str(nextyear)+daystr,'%Y%m%d')
    ls_holidays.append(holiday)
ls_holidays.sort()
# ls_holstr=[datetime.strftime(hol,"%Y-%m-%d") for hol in ls_holidays]
grp_holidays=[]
p=l=0
for i in range(len(ls_holidays)):
    l=i
    if((ls_holidays[i+1]-ls_holidays[i]).days>1):
        grp_holidays.append(ls_holidays[p:l+1])
        p=i+1
grp_holidays.append(ls_holidays[p:l+1])
print(len(grp_holidays))
ls_holstr=[[datetime.strftime(hol,"%Y-%m-%d") for hol in grp] for grp in grp_holidays]
config_val=';\n'.join([','.join(grp) for grp in ls_holstr]) + ';'
print(config_val)

config_str=template.format(nextyear,config_val)
print(config_str)


# from urllib.request import Request, urlopen

# # 包装头部
# firefox_headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'
# }
# # 构建请求
# request = Request(holiday_url, headers=firefox_headers)
# html = urlopen(request)
# # 获取数据
# data = html.read()
# # 转换成字符串
# strs = str(data)
# datas = json.dumps(strs)
# data_json = json.loads(strs)
