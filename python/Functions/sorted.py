numbers = [1,5,7,23,78,87,64,3]

# numbers.sort()


result = sorted(numbers)
result = sorted(numbers, reverse = True) # reverse sorted list
result = sorted((1,53,45,87,97,5,7))

users = [
    {"username": "johndoe" ,"tweets": ["tweet1","tweet2"], "email": "johndoe123@gmail.com"}, # 3 keys username,tweets and email
    {"username": "johndoe123" , "tweets":[] }, # 2 keys username and tweets
    {"username": "johndoe789" ,"tweets": ["tweet1","tweet2","tweet3"], "email": "johndoe123@gmail.com","phonenumber": "345631563"}# 4 keys username,tweet,email and phone number    
]

result = sorted(users, key = len)
result = sorted(users, key = len, reverse=True)
result = sorted(users,key = lambda user:user["username"])
result = sorted(users, key = lambda user: len(user["tweets"]))

courses = [
    {"title": "Python Course", "students": 25000},
    {"title": "Web Development Course", "students": 35000},
    {"title": "Java course", "students": 5000}
]

result = sorted(courses, key = lambda course: course["students"])
result = sorted(courses, key = lambda course: course["students"],reverse = True) # printing with reverse
result = map(lambda course:course["title"], sorted(courses, key = lambda course: course["students"])) # printing the titles of the courses with popularity

print(list(result))