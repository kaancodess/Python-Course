import random

class Question: 
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer


    def checkAnswer(self,answer):
        if answer not in self.choices:
            raise ValueError("Wrong information")
        return self.answer == answer

class Quiz:
    def __init__(self,questions):
        self.questions = random.sample(questions, len(questions))
        self.questionIndex = 0
        self.score = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]
    
    def displayQuestion(self):
        question = self.getQuestion()

        print(f"Question number {self.questionIndex + 1}: {question.text}")

        for q in question.choices:
            print("=) " + q)

        answer = input("Answer: ")
        if (question.checkAnswer(answer)):
            self.score += 10
        else:
            self.score -= 10
        self.questionIndex += 1

        if len(self.questions) == self.questionIndex:
            print(f"your score is: {self.score}")

        else:
            self.displayQuestion()


q1 = Question("2+2",["4", "5","6"],"4")
q2 = Question("2+3",["4", "5","6"],"5")
q3 = Question("3+3",["4", "5","6"],"6")

quiz_questions  = [q1,q2,q3]

quiz = Quiz(quiz_questions)

print(quiz.displayQuestion())