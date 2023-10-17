numbers = [1,2,5,7,9]
str_numbers = ['1','3','6','7','9']
negative_numbers = [-1,-3,-5,-7]
names = ["john" , "michael", "george"]
user = [
    {"name": "John", "surname": "Brown"},
    {"name": "Michael", "surname":"Brown"}
]
# square = []

# for n in numbers:
#     square.append(n ** 2)

# print(square)

# def getSquare(number):
#     return number ** 2

result = list(map(lambda number: number ** 2,numbers))
result = list(map(int, str_numbers)) # string to int
result = list(map(float, str_numbers)) # string to float
result = list(map(abs, negative_numbers)) # return negative numbers to positive with abs
result = list(map(len, names)) # printing  how many letters do they have
result = list(map(str.capitalize, names)) # printing the names list with the first letter big
result = list(map(str.lower,names)) # printing the names list with the first letter lower
result = list(map(lambda x:x["name"],user)) # printing the users name
print(result)