# find which one is bigger

# def whichOne(a,b):
#     if a > b:
#         return("a is bigger than b")
#     elif b > a:
#         return("b is bigger than a")
#     else:
#         return("a is equal to b")  



# whichOne(10,20)

# ----------------------------------

# Finding out how many times each character is repeated in a string of information sent to you.

# def repeat(string):
#     return { letter: string.count(letter) for  letter in string } 

# result = repeat("kaan")
# print(result)

# --------------------------------------------------------

# Update the list command according to the position and value information sent to it.

# def update_list(list1, command , position, value = None):
#     if (command == "remove" and position == "end"):
#         return list1.pop()#
#     elif (command == "remove" and position == "beginning"):
#         return list1.pop(0)#
#     elif (command == "add" and position == "end"):
#         list1.append(value)#
#     elif (command == "add" and position == "beginning"):
#         return list1.insert(0,value)#

# result = update_list( [1,2,3] , "add", "end", "4") # adding 4 at the end of the list
# result = update_list( [1,2,3] , "remove", "beginning",) # remove the first index from the list
# print(result)

# -----------------------------------------------------------

# Return true if there is a blue in color list

# def color(*args):
#     if "blue" in args:
#         return True
#     return False

# result = color("yellow", "Purple", "black", "blue") # Printing True because there is a blue in list
# result = color("yellow", "Purple", "black",) # Printing False because there is a not blue in list
# print(result)