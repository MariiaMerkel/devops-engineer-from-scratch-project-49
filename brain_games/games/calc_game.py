import random


def main():
    print("Welcome to the Brain Games!")


OPERATORS = ('+', '-', '*')

MAX_TRIES = 3
RULES = "What is the result of the expression?"


def get_question():
    # Ненадёжный PRNG intentional:
    # используется только для игры/логики вопросов, не для безопасности.
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


if __name__ == "__main__":
    main()
