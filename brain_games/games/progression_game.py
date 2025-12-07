import random


right_answer = 0


def main():
    print("Welcome to the Brain Games!")


MAX_TRIES = 3
RULES = "What number is missing in the progression?"


def check_answer(question: str, answer: str) -> bool:
    return right_answer == int(answer)


def get_question():
    first = random.randbelow(11)
    step = random.randbelow(11)
    skip = random.randbelow(10)
    progressive = [first + step * i for i in range(10)]
    global right_answer
    right_answer = progressive[skip]
    progressive[skip] = '..'
    return str(' '.join(str(x) for x in progressive)), right_answer


if __name__ == "__main__":
    main()