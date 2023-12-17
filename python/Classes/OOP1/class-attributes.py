class User:
    active_user = 0

    def __init__(self,name,lastname,age):
        self.name = name    
        self.lastname = lastname    
        self.age = age
        User.active_user += 1

    def full_name(self):
        return f"{self.name} {self.lastname}"
    
    def log_out(self):
        User.active_user -= 1
        return f"{self.full_name} is log out"
    
print(User.active_user)
user1 = User("Kaan","Guzel",20)
user2 = User("John","Doe",33)
user3 = User("Maggie","Grimes",33)
print(User.active_user)
user3.log_out()
print(User.active_user)