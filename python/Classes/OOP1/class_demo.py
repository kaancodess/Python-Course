class Comment:
    def __init__(self,username,text,likes = 0,dislikes = 0):
        self.username = username
        self.text = text
        self.likes = likes
        self.dislikes = dislikes
comment1 = Comment("kaanguzel","today is a good day",100,10)
comment2 = Comment("kaangzl","today is a bad day",50,60)
comment3 = Comment("kaangzl123","today is a awful day",300,20)
comment4 = Comment("kaangzl123","today is a beautiful day")

comments = [comment1,comment2,comment3,comment4]

for c in comments:
    print(f"{c.username} commented {c.text} and get {c.likes} likes and {c.dislikes} dislikes")