class Person:
    def __init__(self,name,surname,age):
        self.name = name
        self.surname = surname
        self.age = age
        print("Person Object Created")

    def intro(self):
        print(f"My name is {self.name} {self.surname} and i am {self.age} years old")

class Student(Person):
    def __init__(self,name,surname,age,number):
        super().__init__(name,surname,age)
        self.number = number
        print("Student Object Created.")
    
    def study(self):
        print(f"number {self.number} is study right now.")

class Teacher(Person):
    def __init__(self,name,surname,age,branch):
        super().__init__(name,surname,age)
        self.branch = branch
        print("Teacher Object Created")
    
    def teach(self):
        print(f"Teacher {self.name} is teaching {self.branch} right now.")

p1 = Person("John","Doe",20)
p1.intro()
s1 = Student("Kaan","Guzel",18,89)
s1.intro()
print(s1.number)
t1 = Teacher("Jack","Doe",34,"Mathematics")
t1.intro()
print(t1.branch)
s1.study()
t1.teach()
