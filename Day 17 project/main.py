#Next 3 lines are to import the classes from the other files
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for el in question_data:
    #Setting up the values to put inside the Question object
    question_text = el["question"]
    question_answer = el["correct_answer"]

    #This statement adds the text and answer to the Question object from the question_model.py file
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

#Setting that quiz has the list and the current question being 0 from within the QuizBrain class in the quiz_model.py file
quiz = QuizBrain(question_bank)

while quiz.still_has_questions() == True:
    quiz.next_question()

print("You completed the quiz!")
print(f"Your final score was {quiz.score}/{quiz.question_number}")