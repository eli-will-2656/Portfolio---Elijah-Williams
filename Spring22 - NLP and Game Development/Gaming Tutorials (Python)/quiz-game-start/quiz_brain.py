""" A module to define the quiz class """


class QuizBrain:
    """ A class to ask questions to a user """

    def __init__(self, questions_list):
        self.question_num = 0
        self.question_list = questions_list
        self.questions_right = 0

    def next_question(self):
        current_question = self.question_list[self.question_num]

        answer = input(f"Q.{self.question_num + 1}: {current_question.question} (true/false)?: ")

        self.print_answer(answer)

        self.question_num += 1

    def still_has_questions(self):
        return self.question_num != len(self.question_list)

    def print_answer(self, user_answer):
        if user_answer and user_answer.title()[0] == self.question_list[self.question_num].answer[0]:
            print("You got it correct!")
            self.questions_right += 1
        else:
            print("Sorry, you got it wrong!")

        print(f"The correct answer is: {self.question_list[self.question_num].answer}")

        if self.still_has_questions():
            print(f"Your current score is: {self.questions_right}/{self.question_num + 1}")
        print()








