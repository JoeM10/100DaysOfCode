class QuizBrain:
  def __init__(self, qList):
    self.questionNumber = 0
    self.score = 0
    self.questionList = qList
  
  def stillHasQuestions(self):
    return self.questionNumber < len(self.questionList)

  def nextQuestion(self):
    currentQuestion = self.questionList[self.questionNumber]
    self.questionNumber += 1
    userAnswer = input(f"Q.{self.questionNumber}: {currentQuestion.text} (True/False): ").lower()
    self.checkAnswer(userAnswer, currentQuestion.answer)

  def checkAnswer(self, userAnswer, correctAnswer):
    if userAnswer.lower() == correctAnswer.lower():
      print("You got it right!")
      self.score += 1
    else:
      print("You got it wrong.")
    print(f"The correct answer was: {correctAnswer}.")
    print(f"Your current score is: {self.score}/{self.questionNumber}")
    print("\n")