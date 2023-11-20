import re
# re module 

str = "john doe: johndoe123@gmail.com || age 40"

# ------------------------------

# re.findall()

# result = re.findall("john",str)
# print(result)

# ------------------------------

# re.split()

# result = re.split("doe123",str) # split
# print(result)

# -------------------------------

# re.sub()

# result = re.sub(" ", "-",str)
# result = re.sub("\s", "-",str) # \s means space also too
# print(result)

# -------------------------------

# re.search

# result = re.search("john",str) # find the first john in the str
# result = result.span() # getting the search in list way
# result = result.start() # getting the search information in index way (like it starts in 3...)
# result = result.end() # getting the search end information in index way
# result = result.group() # getting the search find
# result = result.string # get the str information which we gave
# print(result)

# regular expression

