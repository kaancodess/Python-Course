list1 = [13,64,51,36,4]

numbers = []

for i in range(10):
    i *= 2
    numbers.append(i)

# [expression for item in list]
# numbers = [i*i for i in range(10)]

numbers = [i*2 for i in list1] 

name = "Kaan"

names = ["John","Jennifer","Phil"]

result  = [c.upper() for c in name]
result1 = [k.lower()for k in names]

print(result1)