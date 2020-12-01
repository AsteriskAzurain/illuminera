m=eval(input("month:\t"))
d1=eval(input("day start:\t"))
d2=eval(input("day end:\t"))

ls_days=[]
for i in range(d1,d2+1):
    ls_days.append("2021-{}-{}".format("%02d"%m,"%02d"%i))
print(','.join(ls_days))