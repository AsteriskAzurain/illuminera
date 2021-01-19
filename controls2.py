controls=set()

InitForm=[
    'CbDepartment',
	'tbLbApplyUser',
	'CbNumber',
	'City',
	'CbPVNumber',
	'btnConfirm',
	'RadDatePicker1',
	'rdDate',
	'btnSub',
	'btnSave',
	'LbMedicalQuto',
	'MedicalQutoValue'
]
controls.update(InitForm)

CbNumber_SelectedIndexChanged=[
    'LbPvNumber',
	'CbPVNumber',
	'DLIsPV',
	'LbIsPV',
	'DLIsPV',
	'CbPVNumber',
	'LBPVAmount',
	'LBPVAmountSurplus',
	'LBPV',
	'LBPVSurplus',
	'LBCF',
	'LBCFAmount',
	'BtPVView',
	'CbDepartment',
	'CbPaymentCategory',
    'LbCompan'
]
controls.update(CbNumber_SelectedIndexChanged)

DLIsPV_SelectedIndexChanged=[
    'LbPvNumber',
    'CbPVNumber',
    'CbDepartment',
    'BtPVView',
    'LBPVAmount',
    'LBPVAmountSurplus',
    'LBPV',
    'LBPVSurplus',
    'LBCF',
    'LBCFAmount'
]
controls.update(DLIsPV_SelectedIndexChanged)

BtSaveDetail_Click=[
    'LBCFAmount',
    'LBPVAmountSurplus',
    'RgCFDetailInfo'
]
controls.update(BtSaveDetail_Click)

RgCFDetailInfo_DeleteCommand=[
    'RgCFDetailInfo',
    'LBPVAmount',
    'LBCFAmount',
    'LBPVAmountSurplus'
]
controls.update(RgCFDetailInfo_DeleteCommand)

RgCFDetailInfo_NeedDataSource=['RgCFDetailInfo']

RgCFDetailInfo_PageIndexChanged=['RgCFDetailInfo']

RgCFDetailInfo_UpdateCommand=[
    'RgCFDetailInfo',
    'LBPVAmount',
    'LBCFAmount',
    'LBPVAmountSurplus'
]
controls.update(RgCFDetailInfo_UpdateCommand)

SaveData=['RgCFDetailInfo']

btnSave_Click=['CFNumber'] 
btnSub_Click=[]
btnPrint_Click=[]
btnConfirm_Click=[]
btnRefuse_Click=[]
btnFinancePrint_Click=[]
btnFinance_Click=[]
NoAjax=['btnSave','btnSub','btnPrint','btnConfirm','btnRefuse','btnFinancePrint','btnFinance']

CbPVNumber_SelectedIndexChanged=[
    'LBPVAmount',
    'LBPVAmountSurplus',
    'BtPVView',
    'LBPVAmount',
    'LBPV',
    'LBPVSurplus',
    'LBCF',
    'LBCFAmount',
    'CbDepartment',
    'CbPaymentCategory',
    'RgCFDetailInfo'
]
controls.update(CbPVNumber_SelectedIndexChanged)

CbDepartment_SelectedIndexChanged=[
    'CbPaymentCategory',
    'LbCompany'
]
controls.update(CbDepartment_SelectedIndexChanged)

Rcb_IsProject_SelectedIndexChanged=[
    'rdDate',
    'CbNumber',
    'CbPaymentCategory',
    'LbJobNumber',
    'LbPvNumber',
    'CbPVNumber',
    'DLIsPV',
    'LbIsPV',
    'CbDepartment',
    'LbMedicalQuto',
    'Rcb_IsProject',
    'LBPVAmount',
    'LBPVAmountSurplus',
    'LBPV',
    'LBPVSurplus',
    'LBCF',
    'LBCFAmount',
    'BtPVView'
]
DetailControlStatus_Enabled=[
    'rdDate',
    'City',
    'CbPaymentCategory',
    'tbPrice',
    'tbRemarks',
    'BtSaveDetail'
]
Rcb_IsProject_SelectedIndexChanged.extend(DetailControlStatus_Enabled)
controls.update(Rcb_IsProject_SelectedIndexChanged)

controls=dict.fromkeys(controls)

ls_funs=[
    'CbNumber_SelectedIndexChanged',
    'DLIsPV_SelectedIndexChanged',
    'BtSaveDetail_Click',
    'RgCFDetailInfo_DeleteCommand',
    'RgCFDetailInfo_NeedDataSource',
    'RgCFDetailInfo_PageIndexChanged',
    'RgCFDetailInfo_UpdateCommand',
    'btnSave_Click',
    'btnSub_Click',
    'btnPrint_Click',
    'btnConfirm_Click',
    'btnRefuse_Click',
    'btnFinancePrint_Click',
    'btnFinance_Click',
    'CbPVNumber_SelectedIndexChanged',
    'CbDepartment_SelectedIndexChanged',
    'Rcb_IsProject_SelectedIndexChanged'
]

for fn in ls_funs:
    n='_'.join(fn.split('_')[:-1])
    if n not in NoAjax and n in controls.keys():
        if controls[n]==None:
            controls[n]=set()
        controls[n].update(eval(fn))
# ls_controls=[{k:list(v)} for k,v in controls.items() if v!=None]

# import json
# with open("jsonFile3.json","w+") as jf:
#     jf.write(json.dumps(ls_controls,indent=4))

ajaxManagerStr="""
<telerik:AjaxSetting AjaxControlID="{0}">
    <UpdatedControls>
        <telerik:AjaxUpdatedControl ControlID="{0}" />{1}
    </UpdatedControls>
</telerik:AjaxSetting>
"""
ajaxUpdatedControlStr="\n\t\t<telerik:AjaxUpdatedControl ControlID='{0}' />"

outputstr=""
for k,v in controls.items():
    if v != None:
        cstr=""
        for c in v:
            cstr+=(ajaxUpdatedControlStr.format(c))
        outputstr+=ajaxManagerStr.format(k,cstr)
    else:
        outputstr+=ajaxManagerStr.format(k,"")

print(len(outputstr))

f_dst = open(r"ajaxSetting.txt", 'w+',encoding="utf-8")
print(outputstr,file=f_dst)
f_dst.close()