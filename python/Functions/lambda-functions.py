def multiply(a):
    return a ** 2

# print(multiply(4))

# result = (lambda a: a ** 2)(3)

# multiply = lambda a: a ** 2

# result = multiply(5)

sum = lambda a,b,c: a+b+c

result = sum(1,4,7)

reverseStr = lambda s: s[::-1]

result = reverseStr("Kaan")

def myFunc(n):
    return lambda a: a * n

multiply2 = myFunc(2)
multiply3 = myFunc(3)

# result = multiply2(10)
result = multiply3(10)


print(result)