import prompt
import random


def main():
    print("Welcome to the Brain Games!")


OPERATORS = ('+', '-', '*', '/', '%')

MAX_TRIES = 3
RULES = "What is the result of the expression?"


def check_answer(question: str, answer: str) -> bool:
    calculation = calculation_of_expression(question)
    return calculation == int(answer)


def get_question():
    operator = random.choice(OPERATORS)
    match operator:
        case '+':
            first = random.randint(0, 100)
            second = random.randint(0, 100)
            correct_answer = int(first + second)
        case '-':
            second = random.randint(0, 100)
            first = second + random.randint(0, 50)
            correct_answer = int(first - second)
        case '*':
            second = random.randint(0, 20)
            first = second + random.randint(0, 20)
            correct_answer = int(first * second)

    return str(f"{first} {operator} {second}"), correct_answer

def calculation_of_expression(question:str) -> int:
    first, operator, second = question.split(' ')

    match operator:
        case '+':
            return int(first) + int(second)
        case '-':
            return int(first) - int(second)
        case '*':
            return int(first) * int(second)
        case '/':
            return int(first) / int(second)
        case '%':
            return int(first) % int(second)

if __name__ == "__main__":
    main()