class Person:
    #Constructor
    def __init__(self,name,surname,year):
        # Object attributes
        self.name = name
        self.surname = surname
        self.year = year
        
    # instance methods
    def intro(self):
        return f"My name is {self.name} and my surname is {self.surname} and i was born at {self.year}"
    
    def calculateAge(self):
        return f"{2023-self.year}"
    
# Object , Instance
p1 = Person("Kaan","Guzel",2003)
p2 = Person("John","Doe",1999)

print(p1.intro())
print(p2.intro())

print(p1.calculateAge())