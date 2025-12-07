import random


def main():
    print("Welcome to the Brain Games!")


MAX_TRIES = 3
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def check_answer(question: int, answer: str) -> bool:
    return (question % 2 == 0 and answer == "yes") or (
        question % 2 == 1 and answer == "no"
    )


def get_question():
    question = random.randbelow(101)
    return question, "yes" if question % 2 == 0 else "no"


if __name__ == "__main__":
    main()
