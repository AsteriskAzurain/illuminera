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
sql = " select Id,CostingInfoId,SubcontractId from t_PMS_ProjectCosting_ContractNumber where Id > 15232 "

cursor.execute(sql)
ls_all_contract = cursor.fetchall()

ls_dict_upd = []
updateSql = " update t_PMS_ProjectCosting_ContractNumber set ContractAmount={amount} where Id={id} "
query = " SELECT SUM(Number*Rate+Others) FROM t_PMS_SubcontractCostingInfo WHERE CityNameId={subId} AND CostingInfoId={costId} "

for c in ls_all_contract:
    executeDict = {'enable': True}
    try:
        id = c[0]
        costId = c[1]
        subId = c[2]
        executeDict.update({'id': id, 'costId': costId, 'subId': subId})
        cursor.execute(query.format(**executeDict))
        amount = cursor.fetchone()
        executeDict.update({'amount': amount[0]})
    except Exception:
        executeDict.update({'enable': False})
    finally:
        executeDict.update({'enable': ("amount" in executeDict.keys() and executeDict['amount'] != None and executeDict['amount']>0)})
        ls_dict_upd.append(executeDict)

# pprint.pprint(ls_dict_upd)

for dict in ls_dict_upd:
    if dict['enable']:
        u_sql=updateSql.format(**dict)
        # print(u_sql)
        cursor.execute(u_sql)
        conn.commit()
