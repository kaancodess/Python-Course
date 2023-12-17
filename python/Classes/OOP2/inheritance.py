class Person:
    def __init__(self,name,surname,age):
        self.name = name
        self.surname = surname
        self.age = age
        print("Person object created")

    def intro(self):
        print(f"My name is {self.name} {self.surname} and i am {self.age} years old")

class Student(Person):
    pass

class Teacher(Person):
    pass

p1 = Person("John","Doe",20)
p1.intro()
s1 = Student("Kaan","Guzel",18)
s1.intro()
t1 = Teacher("Jack","Doe",34)
t1.intro()
