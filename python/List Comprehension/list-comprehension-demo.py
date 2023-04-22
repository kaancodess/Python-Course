#Find numbers from 1 to 100 that are divisible by 12
result = [k for k in range(1,101) if k % 12 == 0]

names = ["John","Alex","Gilfoyle","Sarah"]
# return the names all lower case and reverse
result = [k.lower() [::-1] for k in names]

string = "Hello 12345 World"
# return the only digit ones
result = [i for i in string if i.isdigit()]

years = [1983,1999,2008,1956,1986]
# return the age from now
import datetime
now = datetime.datetime.now().year
result = [now-year for year in years] 

degrees = [20,5,15,-2,0,-6]
# print "danger of icing" for the weather
result = [degree if degree > 0  else"danger for icing" for degree in degrees]

print(result)