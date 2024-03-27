import datetime
import time
print(time.time())
print(time.asctime())
rr=datetime.datetime.now()
print(rr)
import calendar
s=calendar.isleap(2020)
print(s)
se=calendar.prcal(2024)
x=datetime.datetime.now()
from datetime import timedelta
print(x + timedelta(days=-89))
import pytz
time1=pytz.timezone('Europe/Berlin')
print("Current Time is:", datetime.now(time1))