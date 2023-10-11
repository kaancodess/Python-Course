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

def myFunc(a,b,c,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

myFunc(10,20,30,40,50,60,key1= "value1", key2 = "value2")