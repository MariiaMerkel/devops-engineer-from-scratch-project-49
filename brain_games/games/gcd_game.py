import random
import math


def main():
    print("Welcome to the Brain Games!")


OPERATORS = ('+', '-', '*', '/', '%')

MAX_TRIES = 3
RULES = "Calculate the greatest common divided and input result."


def check_answer(question: str, answer: str) -> bool:
    calculation = calculation_of_expression(question)
    return calculation == int(answer)


def get_question():
    return str(f"{random.randint(1, 100)} {random.randint(1, 100)}")

def calculation_of_expression(question:str) -> int:
    first, second = question.split(' ')
    return math.gcd(int(first), int(second))

if __name__ == "__main__":
    main()