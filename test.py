import datetime
from  datetime  import  timedelta

# 本周第一天
def this_week_start(sDate = datetime.datetime.now().strftime('%Y%m%d')):
    date = datetime.datetime.strptime(sDate, "%Y%m%d").date()
    return (date - timedelta(days = date.weekday())).strftime('%Y%m%d')

# 本周最后一天
def this_week_end(sDate = datetime.datetime.now().strftime('%Y%m%d')):
    date = datetime.datetime.strptime(sDate, "%Y%m%d").date()
    return (date + timedelta(days = 6-date.weekday())).strftime('%Y%m%d')

#上周第一天
def last_week_start(sDate = datetime.datetime.now().strftime('%Y%m%d')):
    date = datetime.datetime.strptime(sDate, "%Y%m%d").date()
    return (date - timedelta(days = date.weekday() + 7)).strftime('%Y%m%d')

#上周最后一天
def last_week_end(sDate = datetime.datetime.now().strftime('%Y%m%d')):
    date = datetime.datetime.strptime(sDate, "%Y%m%d").date()
    return (date - timedelta(days = date.weekday() + 1)).strftime('%Y%m%d')

#本月第一天
def this_month_start(sDate = datetime.datetime.now().strftime('%Y%m%d')):
    date = datetime.datetime.strptime(sDate, "%Y%m%d").date()
    return (datetime.datetime(date.year, date.month,  1 )).strftime('%Y%m%d')

#本月最后一天
def this_month_end(sDate = datetime.datetime.now().strftime('%Y%m%d')):
    date = datetime.datetime.strptime(sDate, "%Y%m%d").date()
    return (datetime.datetime(date.year, date.month  +  1 ,  1 )  -  timedelta(days = 1 )).strftime('%Y%m%d')

#上月第一天
def last_month_start(sDate = datetime.datetime.now().strftime('%Y%m%d')):
    return (datetime.datetime(datetime.datetime.strptime(last_month_end(sDate), "%Y%m%d").date().year, datetime.datetime.strptime(last_month_end(sDate), "%Y%m%d").date().month,  1 )).strftime('%Y%m%d')

#上月最后一天
def last_month_end(sDate = datetime.datetime.now().strftime('%Y%m%d')):
    return (datetime.datetime.strptime(this_month_start(sDate), "%Y%m%d").date()  -  timedelta(days = 1 )).strftime('%Y%m%d')

#本季第一天
def this_quarter_start(sDate = datetime.datetime.now().strftime('%Y%m%d')):
    date = datetime.datetime.strptime(sDate, "%Y%m%d").date()
    month  =  (date.month  -  1 )  -  (date.month  -  1 )  %  3  +  1
    return (datetime.datetime(date.year, month,  1 )).strftime('%Y%m%d')

#本季最后一天
def this_quarter_end(sDate = datetime.datetime.now().strftime('%Y%m%d')):
    date = datetime.datetime.strptime(sDate, "%Y%m%d").date()
    month  =  (date.month  -  1 )  -  (date.month  -  1 )  %  3  +  1
    return (datetime.datetime(date.year, month  +  3 ,  1 )  -  timedelta(days = 1 )).strftime('%Y%m%d')

#上季第一天
def last_quarter_start(sDate = datetime.datetime.now().strftime('%Y%m%d')):
    return (datetime.datetime(datetime.datetime.strptime(last_quarter_end(sDate), "%Y%m%d").date().year, datetime.datetime.strptime(last_quarter_end(sDate), "%Y%m%d").date().month  -  2 ,  1 )).strftime('%Y%m%d')

#上季最后一天
def last_quarter_end(sDate = datetime.datetime.now().strftime('%Y%m%d')):
    return (datetime.datetime.strptime(this_quarter_start(sDate), "%Y%m%d").date() -  timedelta(days = 1 )).strftime('%Y%m%d')

#本年第一天
def this_year_start(sDate = datetime.datetime.now().strftime('%Y%m%d')):
    date = datetime.datetime.strptime(sDate, "%Y%m%d").date()
    return (datetime.datetime(date.year,  1 ,  1 )).strftime('%Y%m%d')

#本年最后一天
def this_year_end(sDate = datetime.datetime.now().strftime('%Y%m%d')):
    date = datetime.datetime.strptime(sDate, "%Y%m%d").date()
    return (datetime.datetime(date.year  +  1 ,  1 ,  1 )  -  timedelta(days = 1 )).strftime('%Y%m%d')

#去年第一天
def last_year_start(sDate = datetime.datetime.now().strftime('%Y%m%d')):
    return (datetime.datetime(datetime.datetime.strptime(last_year_end(sDate), "%Y%m%d").date().year,  1 ,  1 )).strftime('%Y%m%d')

#去年最后一天
def last_year_end(sDate = datetime.datetime.now().strftime('%Y%m%d')):
    return (datetime.datetime.strptime(this_year_start(sDate), "%Y%m%d").date() -  timedelta(days = 1 )).strftime('%Y%m%d')

text = '20210106'
print('本周第一天:' + this_week_start(text))
print('本周最后一天:' + this_week_end(text))

print('上周第一天:' + last_week_start(text))
print('上周最后一天:' + last_week_end(text))

print('本月第一天:' + this_month_start(text))
print('本月最后一天:' + this_month_end(text))

print('上月第一天:' + last_month_start(text))
print('上月最后一天:' + last_month_end(text))

print('本季第一天:' + this_quarter_start(text))
print('本季最后一天:' + this_quarter_end(text))

print('上季第一天:' + last_quarter_start(text))
print('上季最后一天:' + last_quarter_end(text))

print('本年第一天:' + this_year_start(text))
print('本年最后一天:' + this_year_end(text))

print('上年第一天:' + last_year_start(text))
print('上年最后一天:' + last_year_end(text))