import prompt
import random


def main():
    print("Welcome to the Brain Games!")


OPERATORS = ('+', '-', '*', '/', '%')

MAX_TRIES = 3
RULES = "Calculate the expression and input result."


def check_answer(question: str, answer: str) -> bool:
    calculation = calculation_of_expression(question)
    return calculation == int(answer)


def get_question():
    operator = random.choice(OPERATORS)
    match operator:
        case '+':
            first = random.randint(0, 100)
            second = random.randint(0, 100)
        case '-':
            second = random.randint(0, 100)
            first = second + random.randint(0, 50)
        case '*':
            second = random.randint(0, 20)
            first = second + random.randint(0, 20)
        case '/':
            second = random.randint(1, 20)
            first = second * random.randint(0, 10)
        case '%':
            second = random.randint(1, 20)
            first = second * random.randint(0, 10) + random(0, second)

    return str(f"{first} {operator} {second}")

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