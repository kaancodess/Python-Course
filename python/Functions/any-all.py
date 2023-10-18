result = all([False,True,True]) # printing False because there is a False in list
result = any([False,True,True]) # printing True because there is one True in the list

numbers = [0,1,3,6,7,5,67,88,64]

result = all([bool(number) for number in numbers]) # printing False because there is a 0 in the list (the zero is false because its not a integer)

result = any([bool(number) for number in numbers]) # printing True because there is one integer in the list
result = all([bool(number) for number in numbers if number % 2 == 0]) # printing False because there is a False value(0) in the list
result = all([bool(number) for number in numbers if number % 2 == 1]) # printing True because all is True because all of the odd number(integer)

result = any(number % 2 == 0 for number in numbers) # printing true because in the list there is even integers(numbers)

persons = ["John" , "James", "Alexandra"]

result = [person[0] == "J" for person in persons] # pringting [True, True, False] Because the 0 and 1 index start with "J" and index 2 start with "A" so index 2 is a False
result = all([person[0] == "J" for person in persons]) # printing False because there is False value in the list 
result = any([person[0] == "J" for person in persons]) # printing True because there is a True value in the list


print(result)