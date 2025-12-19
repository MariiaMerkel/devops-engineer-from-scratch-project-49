import secrets


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def check_answer(question: int, answer: str) -> bool:
    return (question % 2 == 0 and answer == "yes") or (
        question % 2 == 1 and answer == "no"
    )


def get_question():
    question = secrets.randbelow(101)
    return question, "yes" if question % 2 == 0 else "no"
