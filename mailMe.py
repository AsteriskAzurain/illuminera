import os
from datetime import datetime
now=datetime.now()
day=now.strftime("%m%d")
hour=now.hour

content="\n"

for i in range(hour+1):
    dirname="NeedtoConvert_"+day+("%02d"%i)
    # path="D:/CopyandConvert/"+dirname
    # D:\CopyandConvert_pms\NeedtoConvert_110421
    path="D:/CopyandConvert_pms/"+dirname
    content+=dirname+"    \t    "
    if(os.path.exists(path)):
        length=len([lists for lists in os.listdir(path) if os.path.isfile(os.path.join(path, lists))])
        content+=("filenum: %d \n"%length)
    else:
        content+=("filenum: 0 \n")    
# print(content)


import smtplib
from email.mime.text import MIMEText
#设置服务器所需信息
#163邮箱服务器地址
mail_host = 'smtp.163.com'  
#163用户名
mail_user = 'bevin_fang@163.com'  
#密码(部分邮箱为授权码) 
mail_pass = 'POQTHWWVHQLPXVFR'   
#邮件发送方邮箱地址
sender = 'bevin_fang@163.com'  
#邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
receivers = ['1218081063@qq.com']  

#设置email信息
#邮件内容设置
message = MIMEText(content,'plain','utf-8')
#邮件主题       
message['Subject'] = 'ConvertDocs_'+str(now)
#发送方信息
message['From'] = sender 
#接受方信息     
message['To'] = receivers[0]  

#登录并发送邮件
try:
    smtpObj = smtplib.SMTP() 
    #连接到服务器
    smtpObj.connect(mail_host,25)
    #登录到服务器
    smtpObj.login(mail_user,mail_pass) 
    #发送
    smtpObj.sendmail(
        sender,receivers,message.as_string()) 
    #退出
    smtpObj.quit() 
    print('success')
except smtplib.SMTPException as e:
    print('error',e) #打印错误