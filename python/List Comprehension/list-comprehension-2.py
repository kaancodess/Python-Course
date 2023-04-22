numbers = [3,5,44,77,8]

result = []

for number in numbers:
    if(number % 2 == 0):
        result.append(number)
print(result)

result = [number for number in numbers if number % 2 == 0]
result = [number if  number % 2 == 0 else "odd number" for number in numbers]

print(result)

prices = [1000,3000,5000,4000,0]
taxes = []

taxes = [price*1.18 for price in prices if price > 0]
taxes = [price*1.10 if price > 0 else "tax not calculated" for price in prices]

result = []

for x in range(3):
    for y in range(3):
        result.append((x,y))

result = [(x,y,z) for x in range(3) for y in range(3) for z in range(3)]

print(result)
