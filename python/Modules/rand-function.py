import random 

result = random.random() # random number between 0 and 1
result = random.uniform(10,100) # giving float numbers
result = int(random.uniform(10,100)) # turning float random number to int
result = random.randint(1,100) # random int number

greetings = "Hello there"
names = ["John","Michael","Kate","Alex"]
# result = names[random.randint(0,len(names-1))]
# result = random.choice(names)
# result = random.choice(greetings)

# lst = list(range(10)) # make a list between 0 to 9 
# random.shuffle(lst)

lst = range(100)
result = random.sample(lst, 3) # getting 3 number in lst list
result = random.sample(names, 2) # getting 2 random names in names list

print(result)