import prompt
import random


def main():
    print("Welcome to the Brain Games!")


# NUMBERS = (1, 2, 3, 4, 5, 6, 7, 8, 9)

MAX_TRIES = 3
RULES = "Input 'yes' if number is even and 'no' if number is not even."


def check_answer(question: int, answer: str) -> bool:
    return (question % 2 == 0 and answer == "yes") or (
        question % 2 == 1 and answer == "no"
    )


# def get_question():
#     question = random.randint(1, 9)
#     return question, "yes" if question % 2 == 0 else "no"


if __name__ == "__main__":
    main()
