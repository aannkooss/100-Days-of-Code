from question_model import Question
from data import question_data
from quiz_brain import Quizbrain

questionBank = []
for question in question_data: #creating the question bank
    questionText = question["text"]
    questionAnswer = question["answer"]
    newQuestion = Question(questionText, questionAnswer)
    questionBank.append(newQuestion)

quiz = Quizbrain(questionBank)

while quiz.stillHasQuestions():
    quiz.nextQuestion()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{len(questionBank)}")