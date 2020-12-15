# -*- coding:utf-8 -*-

i=eval(input("月份："))

import calendar
cal=calendar.Calendar()
n=0
dates=cal.itermonthdates(2021,i)
for d in dates:
	if(n%7==0):
		print("\n\n\n\n\n")
	mystr=d.strftime('%m月 %d日')
	print(mystr,end="\t\t")
	n=n+1
