class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def still_has_questions(self):
        #Doing just the return and a statement will return whether it will be True or False
        return self.question_number < len(self.question_list)
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        #The self.question_number += 1 comes before the input becuase it will show Quesiton 1 as the first quesiton instead of 0
        self.question_number += 1
        user_answer = input(f"Question: {self.question_number}: {current_question.question} (True/False): ")
        self.check_answer(user_answer, current_question.answer)
        
        
    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("That's Correct!")
            self.score += 1
        else:
            print("That's Incorrect")
            print(f"The correct answer was {correct_answer}.")
        print(f"Current Score: {self.score}/{self.question_number}\n")