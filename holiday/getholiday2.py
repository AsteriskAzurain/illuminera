from datetime import date
import json
import requests
from datetime import datetime

from requests.models import Response

nextyear = datetime.today().year+1

holiday_url2 = "http://timor.tech/api/holiday/year/{0}".format(nextyear)

# 0工作日 1 假日 2节日
response = requests.get(holiday_url2)
result = response.json()
if(result["code"]==0):
    dict_holiday=result["holiday"]