# get the integer value in the list

# numbers = ["1","2","5a","10b","abc","10","50"]

# for x in numbers:
#     try:
#         result = int(x)
#         print(result)
#     except ValueError:
#         continue

######################################################
# Unless the user enters the q value,
# make sure that every input you receive is a number, otherwise write an error message.

# while True:
#     number = input("number:")
#     if (number == "q"):
#         break

#     try:
#         result = float(number)
#         print(f"entered number {result}")
#         break

#     except ValueError:
#         print("invalid number")
#         break

#######################################################################3
# Write the get function that takes dictionary and key information as parameters.

product = {"product_name": "iphone14"}

def get(d,key):
    try:
        return d[key]
    except KeyError:
        return None
    
print(get(product, "price")) # there is no price value in the dict
print(get(product,"product_name"))