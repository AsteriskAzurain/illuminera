# -*- coding: utf-8 -*-
import pprint
import pymssql

# server = "192.168.1.240\MSSQL240"
server = "weiliu\mysqlserver"
password = "qaz123456wsx"
# server = "localhost"
# password = "Sql12pswd"
# server = "192.168.1.245"
# password = "Illuminera2011"
user = "sa"
database = "IllumineraERP"
conn = pymssql.connect(server, user, password, database, charset='GB2312')

cursor = conn.cursor()
sql = " select Id,CostingInfoId,Agentname from t_PMS_ProjectCosting_ContractNumber where ComponentId is null "

cursor.execute(sql)
ls_all_contract = cursor.fetchall()

ls_dict_upd = []
updateSql = " update t_PMS_ProjectCosting_ContractNumber set ComponentId={comId}, SubcontractId={subId} where Id={id} "
query_1 = " select ComponentId from t_PMS_ProjectCostingInfo where Id={0} "
query_2 = " select ID from t_Base_Subcontract where AgentName=(select Agentname from t_PMS_ProjectCosting_ContractNumber where Id={0}) "
for c in ls_all_contract:
    executeDict = {'enable': True}
    try:
        id = c[0]
        costid = c[1]
        # subName = c[2]
        # subName=subName.encode('gbk')
        cursor.execute(query_1.format(costid))
        comId = cursor.fetchone()
        comId = comId[0]
        # query_2_str=query_2.format(subName)
        # cursor.execute(query_2_str.encode('utf-8').decode('utf-8'))
        cursor.execute(query_2.format(id))
        subId = cursor.fetchone()
        subId = subId[0]
        executeDict.update({'id': id, 'comId': comId, 'subId': subId})
    except Exception:
        executeDict.update({'enable': False})
    finally:
        ls_dict_upd.append(executeDict)

# pprint.pprint(ls_dict_upd)

for dict in ls_dict_upd:
    if dict['enable']:
        u_sql=updateSql.format(**dict)
        # print(u_sql)
        cursor.execute(u_sql)
        conn.commit()
