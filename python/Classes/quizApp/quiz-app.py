class Question: 
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer


    def checkAnswer(self,answer):
        if answer not in self.choices:
            raise ValueError("Wrong information")
        return self.answer == answer

q1 = Question("2+2",["4", "5","6"],"4")

print(q1.text)
print(q1.choices)
print(q1.answer)

result = q1.checkAnswer("5")
print(result)