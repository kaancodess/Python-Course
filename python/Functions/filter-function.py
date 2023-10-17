ages = [3,12,15,18,23,38,55]

def isitTeenager(x):
    if x < 18:
        return False
    else:
        return True
    
# for i in filter(isitTeenager, ages):
#     print(i)

result = list(filter(isitTeenager,ages))

result = list(filter(lambda x: x <= 18, ages))

numbers = [1,2,4,5,7,84,67,53,66,78]

result = list(filter(lambda x : x % 2 == 0 , numbers))

names = ["Alexandra" , "Andrew" , "John"] 

FilteredResult = list(filter(lambda n: n[0] == 'A',names))

result = list(map(lambda n: n.upper(),FilteredResult))

users = [
    {"username":"johndoe", "tweets":["tweet1","tweet2"]},
    {"username":"johndoe123", "tweets":[]},
    {"username":"johndoe123456", "tweets":["tweet s3"]}
]

result = list(filter(lambda u: len(u["tweets"]) > 0,users))

result = list(map(lambda u:u["username"],users)) # if you want everything just use map function but if you want to get something you need you can use filter function

result = [user["username"].upper() for user in users if len(user["tweets"]) > 0]

print(result)