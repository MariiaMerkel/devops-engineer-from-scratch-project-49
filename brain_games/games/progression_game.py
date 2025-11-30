import prompt
import random


right_answer = 0
def main():
    print("Welcome to the Brain Games!")


MAX_TRIES = 3
RULES = "Input the missing element"


def check_answer(question: str, answer: str) -> bool:
    return right_answer == int(answer)


def get_question():
    first = random.randint(1, 10)
    step = random.randint(1, 10)
    skip = random.randint(0, 9)
    progressive = [first + step * i for i in range(10)]
    global right_answer
    right_answer = progressive[skip]
    progressive[skip] = '...'
    return str(', '.join(str(x) for x in progressive))

if __name__ == "__main__":
    main()