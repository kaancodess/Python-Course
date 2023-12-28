#def generate_infinite_number():
#	number = 0
#	while True:
#		yield number
#		number += 1
#
#generator = generate_infinite_number()
#
#print(next(generator)) # 1
#print(next(generator)) # 2
#print(next(generator)) # 3
#
#for i in generator:
#	print(i)

#def fib_list(max):
#	numbers = []
#	
#	a, b = 0,1
#
#	while len(numbers) < max:
#		numbers.append(b)
#		a, b = b , a+b
#	return numbers
#
## print(fib_list(10))
#
#def fib_gen(max):
#	a,b = 0,1
#	count = 0
#	while count < max:
#		a , b = b , a+b
#		yield b
#		count += 1

#import sys
#
#lst = [i*2 for i in range(10000)] 
#print(sys.getsizeof(lst)) # 85176
#
#lst_generator = (i**2 for i in range(1000))
#print(sys.getsizeof(lst_generator)) # 104


import time

list_start_time = time.time()
sum([i**2 for i in range(100000000)])
list_stop = time.time() - list_start_time


gen_start_time = time.time()
sum((i**2 for i in range(100000000)))
gen_stop = time.time() - gen_start_time

print(f"List: {list_stop} , Generator: {gen_stop}")
# List: 23.853245973587036 , Generator: 22.72115993499756 Time Comparison
