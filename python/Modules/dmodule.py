from datetime import datetime
from datetime import timedelta

result = dir(datetime) # getting all the datetime functions

result = datetime.now()

now = datetime.now()

result = now.year
result = now.month
result = now.day
result = now.second
result = datetime.ctime(now) # more specific information
result = datetime.strftime(now,'%A') # getting one information at current time Y > year d > day H > hour M > minute  
# A > getting day information as a string
# B > getting  month information as a string
result = datetime.strftime(now,'%Y %B %A') # getting year , month and day as a string


# t = " 14 November 2023"
# day, month , year = t.split()
# print(day)
# print(month)
# print(year)

t = "14 November 2023 hour 18:06:53"
result = datetime.strptime(t, '%d %B %Y hour %H:%M:%S') 
result = result.year

birthday = datetime(2003,2,19,12,30,10)

result = datetime.timestamp(birthday) # second
result = datetime.fromtimestamp(result) # second to datetime

result = now - birthday # timedelta

# result = result.days

# result = result.seconds
result = result.microseconds

result = now + timedelta(days = 10) # adding 10 days


print(result)