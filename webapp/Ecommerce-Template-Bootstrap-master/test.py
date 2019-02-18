from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta

now = datetime.now()

# for i in range(365):
#     d = datetime.strptime('2019-01-01','%Y-%m-%d')
#     a = timedelta(i)
#     b = (d+a).strftime('%Y-%m-%d')
#     print (b)

month = []
day = []
days = []


for i in range(365):

    d = datetime.strptime('2019-01-01', '%Y-%m-%d')
    e = timedelta(i)
    res = d + e
    res_month = res.strftime("%m")
    res_day = res.strftime("%d")


print (month)
# e = datetime.now()
# d = datetime.strptime('2019-02-14', '%Y-%m-%d')

# if e-d >= timedelta(1):
#     print (e.strftime('%m-%d'))
# else :
#     print (e.strftime('%H:%M'))

# def ymd(fmt):
#     def trans(date_str):
#         return datetime.strptime(date_str, fmt)
#     return trans


# def dt():
#     datestr = request.values.get('date', date.today(), type=ymd('%Y-%m-%d'))
#     return "우리나라 시간   형식: " + str(datestr)



