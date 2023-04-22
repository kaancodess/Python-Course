brands = ["opel","bmw","mercedes"]
# index = 0
# for brand in brands:
#     index += 1
#     print(f"{index}-{brand}")

# enumerate

# obj1 = enumerate(brands)

# print(type(obj1))

# print(list(obj1))

# for index,value in enumerate(brands,1):
#     print(f"{index}-{value}")

list1 = [1,2,3,4,5,]
list2 = ['a','b','c','d','e','f']
list3 = [100,200,300,400,500]

print(list(zip(list1,list2,list3)))


for item in zip(list1,list2,list3):
    print(item)

for a,b,c in zip(list1,list2,list3):
    print(a,b,c)