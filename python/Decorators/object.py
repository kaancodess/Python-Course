def greeting(name):
    print("hello" ,name)

##print(greeting("John"))
#print(greeting)

sayHello = greeting

#print(sayHello) # same adress with greeting
#print(greeting)

del sayHello
#print(sayHello) # NameErrori

# Encapsulation

def outer(num1):
    print("outer")
    def inner_increment(num1):
        print("inner")
        return num1 + 1
    num2 = inner_increment(num1)
    print(num1,num2)
outer(10)
#inner_increment(10) # not defined error

def factorial(number):
    if not isinstance(number,int):
        raise ValueError("Number must be integer")

    if not number >= 0:
        raise ValueError("Number must be zero or positive")

    def inner_factorial(number):
        if number <= 1:
            return 1 
        
        return number * inner_factorial(number - 1)

    return inner_factorial(number)

print(factorial("5"))

