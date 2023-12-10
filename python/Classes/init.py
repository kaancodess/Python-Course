class Product:
    def __init__(self,name , price, isActive = True):
        self.name = name
        self.price = price
        self.isActive = isActive
        print("product object created")

p1 = Product("Iphone 15",3000)
p2 = Product("Iphone 15 Pro" , 3500 , False)

print(p1.name, p1.price, p1.isActive)
print(p2.name, p2.price, p2.isActive)