import json
import sys
from prettytable import PrettyTable
from quiz_brain import QuizBrain

print("This is a simple Quiz Game to test your skills in different topics.")
print("Topics available:")

table = PrettyTable()
table.add_column("Prog. Languages", ["Python", "C Programming"])
table.add_column("DS&A", ["Big O", "_"])

print(table)

# Create a dictionary mapping topics to their respective JSON files
topic_mapping = {
    "python": "python.json",
    "p": "python.json",
    "bigo": "bigO.json",
    "c": "c.json",
    "cprogramming": "c.json",
}

# Get the user's chosen topic and map it to the corresponding JSON file
user_topic = input("Choose a topic: ").lower().strip()
file_name = topic_mapping.get(user_topic)

# Validate user input
while not file_name:
    # print("انا وانت عارفين الل فيها ف انجز الله يهديك احنا لسه ف الاول :)")
    print("Invalid topic. Please choose a valid topic.")
    user_topic = input("Choose a topic: ").lower().strip()
    file_name = topic_mapping.get(user_topic)

# Load the questions from the selected JSON file
with open(file_name, "r") as file:
    question_data = json.load(file)  # type(question_data) => dict

# Clear the console screen
sys.stdout.write('\033c')
sys.stdout.flush()

# Initialize the quiz
quiz = QuizBrain(question_data["questions"])  # type(question_data["questions"]) => list

while quiz.still_has_questions():
    quiz.next_question()

    # Clear the console screen
    sys.stdout.write('\033c')
    sys.stdout.flush()

print("You've ended the quiz.")
print(f'Your final score is: {quiz.get_score()}/{len(question_data["questions"])}')
