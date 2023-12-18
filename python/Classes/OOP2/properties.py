class Product:
    def __init__(self,name,price,description):
        self.name = name
        self.description = description
        if price >=0:
            self._price = price
        else:
            raise ValueError("Price can not be negative.")

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self,value):
        if value >= 0:
            self._price = value
        else:
            raise ValueError("Price can not be negative.")
    
    @property
    def short_description(self):
        return self.description[:10]

    # def set_price(self,value):

    #    if value >=0:
    #        self._price = value

    #    else:
    #        raise ValueError("Price can not be negative.")

    # def get_price(self):
    #    return self._price
    

p1 = Product("Iphone 14",2200,"Iphone 14 is the newest model of Iphones")
# p1.price = -9000
# p1.set_price(-2500) # returning ValueError
print(p1.short_description) # Output: Iphone 14
