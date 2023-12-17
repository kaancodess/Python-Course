class User:

    active_user = 0

    @classmethod
    def display_active_users(cls):
        return f"There is a {cls.active_user} active users right now"
    
    @classmethod
    def from_string(cls,data_str):
        name,surname,age = data_str.split(",")
        return cls(name,surname,age)
    
    def __init__(self,name,lastname,age):
        print(self)
        self.name = name    
        self.lastname = lastname    
        self.age = age
        User.active_user += 1

    def full_name(self):
        return f"{self.name} {self.lastname}"
    
    def log_out(self):
        User.active_user -= 1
        return f"{self.full_name} is log out"

john = User.from_string("John,Doe,33")

print(john.name) # output : John