# Quiz Game (ALX Quizzes)

## Overview

This is a simple Quiz Game designed to test your knowledge in various topics.
It allows users to select a topic, answer questions related to that topic, and see their final score at the end of the quiz.
The project is implemented in Python and uses JSON files to store quiz questions for different topics.

## Features

- Choose from multiple quiz topics.
- Answer a series of multiple-choice questions.
- Check your score at the end of the quiz.
- View your progress and see the remaining questions.
- Easily extendable by adding more quiz questions in JSON format.


## Installation

- Clone the repository to your local machine.

    ```bash
    git clone https://github.com/mdawoud27/alx_quizzes.git
    ```
   
## Usage

1. Run the main script to start the quiz.

    ```bash
    python3 main.py
    ```
   *If there any errors of `prettytable` module, you have to install it*
    ```bash
   pip install prettytable
   ```
    Or take a look [*here*](https://pypi.org/project/prettytable/) for extra info.


2. Choose a quiz topic from the available options (e.g., Python, C Programming, BigO Notation).

3. Answer the quiz questions by entering the number of your answer (e.g., 1, 2, 3) or use 'state' to check your progress or 'off' to end the quiz.

4. After completing the quiz, your final score will be displayed.

5. You can run the quiz again with a different topic or quit the program.

## Customizing the Quiz

*To add more quiz questions or topics:*

1. Create a new JSON file for the topic you want to add (e.g., `topic.json`).

2. Format the JSON file with questions, choices, and correct answers. See existing JSON files for reference.

3. Update the `topic_mapping` dictionary in `main.py` to include your new topic and corresponding JSON filename.

4. Run the main script, choose your new topic, and enjoy the quiz.

## JSON File Structure

*Each JSON file representing a quiz topic **MUST** follow this structure to avoid any bugs or errors:*

```json
{
    "questions": [
        {
            "question": "What is the capital of France?",
            "choices": ["Berlin", "London", "Paris", "Madrid"],
            "correct_answer": "Paris"
        },
        {
            "question": "Which programming language is known for its readability?",
            "choices": ["Java", "C++", "Python", "Ruby"],
            "correct_answer": "Python"
        }
    ]
}
```

## Contributing
If you would like to contribute to this project, please open an issue or submit a pull request with your suggested changes.

Feel free to enhance this `README` with additional sections or details specific to your project.
