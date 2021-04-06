import pymssql

server = "192.168.1.245"
# server = "192.168.1.240\MSSQL240"
user = "sa"
password = "Illuminera2011"
# password = "qaz123456wsx"
database = "IllumineraERP"
conn = pymssql.connect(server, user, password, database)

cursor = conn.cursor()
sql = "select [Jobs_SendMailAttachmentID],[FileName] from [t_Jobs_SendMailAttachments] "

cursor.execute(sql)
ls_allatts = cursor.fetchall()
# conn.close()

ls_dict_upd = []
updateSql = " update t_Jobs_SendMailAttachments set PMS_ProjectCosting_ContractNumberID={cn_id} where Jobs_SendMailAttachmentID={id} "
for att in ls_allatts:
    executeDict = {'enable': True}
    try:
        id = att[0]
        fn = att[1]
        contractNumber = str(fn).split('-')[0]
        executeDict.update({'id': id, 'cn': contractNumber})
    except Exception:
        executeDict.update({'enable': False})
    finally:
        ls_dict_upd.append(executeDict)


querySql = " select Id from t_PMS_ProjectCosting_ContractNumber where ContractNumber='{cn}' "
for dict in ls_dict_upd:
    if dict['enable']:
        q_sql=querySql.format(cn=dict['cn'])
        cursor.execute(q_sql)
        try:
            result=cursor.fetchone()
            dict.update({'cn_id':result[0]})
        except Exception:
            dict.update({'enable': False})

ls_dict_upd = [ d for d in ls_dict_upd if d['enable']]

for upd_d in ls_dict_upd:
    u_sql=updateSql.format(**upd_d)
    # print(u_sql)
    cursor.execute(u_sql)
    conn.commit()

conn.close()

# 验证
# ```sql
# SELECT ATT.Jobs_SendMailAttachmentID,ATT.[PMS_ProjectCosting_ContractNumberID],CN.ContractNumber,ATT.FileName
# FROM t_Jobs_SendMailAttachments ATT
# LEFT JOIN t_PMS_ProjectCosting_ContractNumber CN ON CN.Id=ATT.[PMS_ProjectCosting_ContractNumberID]
# ```