class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        n_question = self.question_list[self.question_number]
        self.question_number += 1
        player_ans = input(f"Q.{self.question_number}: {n_question.text} (True/False): ").lower()
        self.check_answer(player_ans, n_question.answer)

    def check_answer(self, player_answer, correct_answer):
        if player_answer == correct_answer.lower():
            print('You got it right!')
            self.score += 1
        else:
            print("That's wrong!")

        print(f'The correct answer was: {correct_answer}')
        print(f'Your current score is: {self.score}/{self.question_number}')
        print('\n')
