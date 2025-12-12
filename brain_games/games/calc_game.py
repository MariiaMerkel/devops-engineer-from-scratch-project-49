import secrets


def main():
    print("Welcome to the Brain Games!")


OPERATORS = ('+', '-', '*')
RULES = "What is the result of the expression?"


def get_question():
    # Ненадёжный PRNG intentional:
    # используется только для игры/логики вопросов, не для безопасности.
    operator = secrets.choice(OPERATORS)
    match operator:
        case '+':
            first = secrets.randbelow(101)
            second = secrets.randbelow(101)
            correct_answer = int(first + second)
        case '-':
            second = secrets.randbelow(101)
            first = second + secrets.randbelow(51)
            correct_answer = int(first - second)
        case '*':
            second = secrets.randbelow(21)
            first = second + secrets.randbelow(21)
            correct_answer = int(first * second)

    return str(f"{first} {operator} {second}"), correct_answer
