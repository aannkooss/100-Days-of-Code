class Quizbrain:
    def __init__(self, questionList):
        self.questionNumber = 0
        self.questionlist = questionList
        self.score = 0

    def nextQuestion(self):
        currentQuestion = self.questionlist[self.questionNumber]
        self.questionNumber += 1
        answer = input(f"Q.{self.questionNumber}: {currentQuestion.text} (True/False): ")
        self.checkAnswer(answer, currentQuestion.answer)
    def stillHasQuestions(self):
        return self.questionNumber < len(self.questionlist) #an easier way to do an if else statement

    def checkAnswer(self, answer, correctAnswer):
        if answer.lower() == correctAnswer.lower():
            print(" >> You got it right! << ")
            self.score += 1
        else:
            print(" >> Incorrect << ")
        print(f"The correct answer was: {correctAnswer}")
        print(f" >> Current score: {self.score}/{self.questionNumber}")
        print("\n")