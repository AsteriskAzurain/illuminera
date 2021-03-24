from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

from time import sleep
from datetime import datetime

from bs4 import BeautifulSoup
import pymssql

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
driver.get('http://192.168.1.245:8088/login.aspx')
# sleep(3)
WebDriverWait(driver, 10)

username = "wei.liu"
password = "Q1w2e3r4"
# #txtUserName #txtPassword #btnlogin
driver.find_element_by_id('txtUserName').send_keys(username)
driver.find_element_by_id('txtPassword').send_keys(password)
driver.find_element_by_id('btnlogin').click()
sleep(3)

server="192.168.1.245"
user="sa"
password="Illuminera2011"
database="IllumineraERP"
conn = pymssql.connect(server, user, password, database)

cursor = conn.cursor()
sql = "select sqlFileID from [t_Jobs_P2FConvertRecord] where createTime > '{0}'"
sql=sql.format(datetime.now().strftime("%Y-%m-%d"))

cursor.execute(sql)
ls_fileID=cursor.fetchall()
conn.close()

docUrl = "http://192.168.1.245:8088/ARES/SWF_FILE/docviewer.html#{0}.xml"

ls_fail=[]
for fileid in ls_fileID:
    fileid=fileid[0]
    url=docUrl.format(fileid)
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html,features="html.parser")

    textmsg = soup.find('span', id='textmsg').get_text()
    pagelist = soup.find_all('div', attrs={"class": "pagecont"})

    print(fileid,'\t',"Success" if len(pagelist) > 0 else textmsg)
    
    if(len(pagelist)==0): ls_fail.append(fileid)

driver.close()

print('\n\n失败个数:',len(ls_fail))

if (len(ls_fail)): 
    for fail_id in ls_fail: print(fail_id)