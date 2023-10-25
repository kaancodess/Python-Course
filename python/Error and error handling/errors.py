# x = int(input("x: "))  I give x a 10
# y = int(input("y: "))  I deliberately give the y value 20a 
# and this was the error " ValueError: invalid literal for int() with base 10: '20a' "
try:
    x = int(input("x: "))
    y = int(input("y: "))
    print(x + y)
except:
    print("Unknown error. Please try again.") # we catch the error and give the message for the user
