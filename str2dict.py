print("start")
keystr=input();valstr=input()

ls_key=keystr.split("\t") # ; ls_key=['"{0}"'.format(k) for k in ls_key]
ls_val=valstr.split("\t") # ; ls_val=['"{0}"'.format(v) for v in ls_val]

output_dict=dict(zip(ls_key,ls_val))

# 输出单引号
# print(output_dict)

# 输出双引号
# 1
# ls_o=[ '"{k}":"{v}"'.format(k=k,v=v)  for k,v in output_dict.items()]
# print('{',','.join(ls_o),'}')
# 2
print(repr(output_dict).replace("'",'"'))

# rept: Return the canonical string representation of the object.
