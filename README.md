# illuminera
工作用到的脚本

```python
f_dst = open(r"output.txt", 'w+',encoding="utf-8")
print(',\n'.join(ls_swf_id),file=f_dst)
f_dst.close()
```

```sql
update t_Jobs_P2FConvertRecord set status=1,updateTime='2020-12-09 16:40'
where srcTable=1 and sqlID in(1907,1908,1909,1911,1912,6244,1514,456,338,8045,4158,1041,13009,1571,13483,1038,668,669,2045,6769,11410)
```