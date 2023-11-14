from datetime import datetime

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
print(result)

# 31