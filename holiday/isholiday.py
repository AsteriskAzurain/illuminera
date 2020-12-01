import datetime
import chinese_calendar
import calendar
cal=calendar.Calendar()

worktime=dict()
year=2021
insertstr="INSERT INTO t_Fin_TimeSheetStandard(YearMonth,StandardHours) VALUES('{0}', {1})"
for month in range(1,13):
    # 获取当前月的第一天的星期和当月总天数
    weekdays,monthCountDay=calendar.monthrange(year,month)
    hours=0
    for day in range(1,monthCountDay+1):
        if(chinese_calendar.is_workday(datetime.date(year,month,day))):
            hours+=8
    worktime[month]=hours
    print(insertstr.format(str(year)+str(month),hours))  
print(worktime)
# {1: 160, 2: 136, 3: 184, 4: 176, 5: 152, 6: 168, 7: 176, 8: 176, 9: 176, 10: 136, 11: 176, 12: 184}

# INSERT INTO t_Fin_TimeSheetStandard(YearMonth,StandardHours) VALUES('20211', 160)
# INSERT INTO t_Fin_TimeSheetStandard(YearMonth,StandardHours) VALUES('20212', 136)
# INSERT INTO t_Fin_TimeSheetStandard(YearMonth,StandardHours) VALUES('20213', 184)
# INSERT INTO t_Fin_TimeSheetStandard(YearMonth,StandardHours) VALUES('20214', 176)
# INSERT INTO t_Fin_TimeSheetStandard(YearMonth,StandardHours) VALUES('20215', 152)
# INSERT INTO t_Fin_TimeSheetStandard(YearMonth,StandardHours) VALUES('20216', 168)
# INSERT INTO t_Fin_TimeSheetStandard(YearMonth,StandardHours) VALUES('20217', 176)
# INSERT INTO t_Fin_TimeSheetStandard(YearMonth,StandardHours) VALUES('20218', 176)
# INSERT INTO t_Fin_TimeSheetStandard(YearMonth,StandardHours) VALUES('20219', 176)
# INSERT INTO t_Fin_TimeSheetStandard(YearMonth,StandardHours) VALUES('202110', 136)
# INSERT INTO t_Fin_TimeSheetStandard(YearMonth,StandardHours) VALUES('202111', 176)
# INSERT INTO t_Fin_TimeSheetStandard(YearMonth,StandardHours) VALUES('202112', 184)