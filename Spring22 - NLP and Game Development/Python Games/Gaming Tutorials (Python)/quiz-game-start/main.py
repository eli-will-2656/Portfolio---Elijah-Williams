from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
import random


def main():
    # Create question-bank (list of Question objects)
    question_bank = []
    data = random.sample(question_data, 10)

    for question in data:
        text = question['question']
        answer = question['correct_answer']
        new_question = Question(text, answer)
        question_bank.append(new_question)

    quiz = QuizBrain(question_bank)

    while quiz.still_has_questions():
        quiz.next_question()

    print(f"Congradulations for completing the quiz! You answered %.2f"
          " percent of questions correctly!" % (quiz.questions_right / quiz.question_num * 100))


if __name__ == '__main__':
    main()


