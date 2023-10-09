#list = [10,20,30] 

#def sum(numbers):
#    result = 0
#    for i in numbers:
#        result += i
#    return result

#print(sum(list))


def sum(*args):
    print(type(args))
    result = 0
    for i in args:
        result += i
    return result

print(sum(10,20,30))

print(sum(10,20,30,40))


a = 10,20,30

for i in a:
    print(i)