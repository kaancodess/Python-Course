def count_number(max):
	number = 1
	while number <= max:
		yield number
		number += 1

generator = count_number(10)

iterator = iter(generator)

# print(next(iterator)) # 1 
# print(next(iterator)) # 2

# for i in iterator: # and printing the rest with for loop
	# print(i)

# result = list(iterator) # turning into a list 

# print(result)

generator = (i for i in range(1,11))

print(next(generator)) # 1
print(next(generator)) # 2
