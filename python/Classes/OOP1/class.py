# Class


# class Student:
    # method
    # attribute
    # pass

# Object , Instance

# student1 = Student()
# student2 = Student()

# print(student1 , student2) # different addresses on ram memory

class Product: 
    pass
p1 = Product() # Samsung TV 
p2 = Product() # LG TV
p3 = Product() # Apple TV 

products = [p1,p2,p3]

for p in products:
    print(p)
    print(type(p))