# for i in range(1,11):
#     print("**********")
#     for k in range(1,11):
#         print("{} x {} = {}".format(i,k,i*k))

number = int(input("please enter a number: "))

isitPrime = True

if(number == 1):
    isitPrime = False

for i in range(2,number):
    if(number % i == 0):
        isitPrime = False
        break

if isitPrime:
    print("the number is prime number")
else:
    print("the number is not a prime number")