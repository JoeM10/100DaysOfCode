# class User:
#   def __init__(self, userId, username):
#     self.id = userId
#     self.username = username
#     self.followers = 0
#     self.following = 0
  
#   def follow(self, user):
#     user.followers += 1
#     self.following += 1



# user1 = User("001", "Jacob")
# user2 = User("002", "Joe")

# user1.follow(user2)
# print(user1.followers)
# print(user1.following)
# print(user2.followers)
# print(user2.following)

# Quiz Game Project--------

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questionBank = []

for question in question_data:
  questionText = question["question"]
  questionAnswer = question["correct_answer"]
  newQuestion = Question(qText=questionText, qAnswer=questionAnswer)
  questionBank.append(newQuestion)

quiz = QuizBrain(questionBank)
while quiz.stillHasQuestions():
  quiz.nextQuestion()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.questionNumber}")