class QuizBrain:
    """
    A class representing a quiz game.

    Attributes:
        question_number (int): The current question number.
        question_list (list): The list of questions and choices.
        score (int): The player's score.
    """

    def __init__(self, q_list):
        """
        Initialize a new QuizBrain instance.

        Args:
            q_list (list): A list of dictionaries representing questions and choices.
        """
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        """
        Check if there are more questions to answer.

        Returns:
            bool: True if there are more questions, False otherwise.
        """
        return self.question_number < len(self.question_list)

    def next_question(self):
        """
        Display the next question and handle user input for answers.

        - Shows the current question and choices.
        - Validates and processes user input for answers, 'state', or 'off'.
        - Updates the score and question number based on user input.
        """
        while self.question_number < len(self.question_list):
            current_question = self.question_list[self.question_number]
            self.question_number += 1

            # Show the current question
            print(f'Q.{self.question_number}: {current_question["question"]}')

            # Show Choices
            for i, choice in enumerate(current_question["choices"], start=1):
                print(f"{i}. {choice}", end='\t\t')
            print()

            while True:
                user_ans = input(
                    "Enter the number of your answer (e.g., 1, 2, 3, ...), 'state' to see your progress, or "
                    "'off' to end the quiz: ").strip()

                if user_ans.isdigit():
                    user_ans = int(user_ans)
                    if 1 <= user_ans <= len(current_question["choices"]):
                        user_ans = current_question["choices"][user_ans - 1]
                        self.check_ans(user_ans, current_question["correct_answer"])
                        break  # Break the loop and proceed to the next question
                    else:
                        print("Invalid choice. Please enter a valid number.")
                else:
                    if user_ans == "state":
                        print(self.state())  # Show progress
                        # Present the same question again
                        self.question_number -= 1
                        break
                    elif user_ans == "off":
                        self.question_number = len(self.question_list)
                        break  # End the quiz
                    else:
                        print(
                            "Invalid input. Please enter\n\t- The number of the correct answer,\n\t- 'state' to show "
                            "your progress,\n\t- or 'off' to end the quiz.")

            print()

    def check_ans(self, user_ans, correct_ans):
        """
        Check if the user's answer is correct and update the score.

        Args:
            user_ans (str): The user's answer.
            correct_ans (str): The correct answer for the current question.
        """
        if user_ans.lower().strip() == correct_ans.lower().strip():
            self.score += 1

    def state(self):
        """
        Get the user's progress and remaining questions.

        Returns:
            str: A message with the user's progress and remaining questions.
        """
        return (f'\n=> You have {self.get_score()} correct answers, '
                f'{self.question_number - self.get_score() - 1} wrong answers, '
                f'and {len(self.question_list) - self.question_number + 1} remaining questions.')

    def get_score(self):
        """
        Get the player's score.

        Returns:
            int: The player's score.
        """
        return self.score
