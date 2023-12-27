class User:
    
    active_users = 0

    @classmethod
    def display_active_users(cls):
        return f"there is {cls.active_users} active users right now."


    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname
        User.active_users += 1

    def fullname(self):
        return f"{self.firstname} {self.lastname}"

class Moderator(User):

    active_moderators = 0

    @classmethod
    def display_active_moderators(cls):
        return f"there is {cls.active_moderators} active moderators right now."


    def __init__(self,firstname,lastname,community):
        super().__init__(firstname,lastname)
        self.community = community
        Moderator.active_moderators += 1
    
    def remove_post(self):
        return f"Moderator {self.fullname()} removed a post about {self.community}"

    def update_post(self):
        return f"Moderator {self.fullname()} updated a post about {self.community}"

u1 = User("John","Doe")
m1 = Moderator("Kaan","Guzel","Software")

# print(isinstance(u1,User)) # u1 is created by the User class # True
# print(isinstance(u1,Moderator)) # u1 is not created by the Moderator class so it's false


print(User.display_active_users())
print(Moderator.display_active_moderators())
print(m1.remove_post())
print(m1.update_post())
