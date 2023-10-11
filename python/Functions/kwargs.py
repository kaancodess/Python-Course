# def displayUser(*args):
#     print(type(args)) # tuple
#     print(kwargs) # printing this "()" because its a tuple
# displayUser()

def displayUser(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")
    print("\n")

#   print(type(kwargs)) # dict
#   print(kwargs) # printing this "{}" because its a dict


displayUser(username = "kaanguzel") 
displayUser(username = "kaanguzel" ,email = "test1234@gmail.com")
displayUser(username = "kaanguzel" ,email = "test1234@gmail.com", country = "Turkey")