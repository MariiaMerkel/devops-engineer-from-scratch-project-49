import random


def main():
    print("Welcome to the Brain Games!")


MAX_TRIES = 3
RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def check_answer(number) -> bool:
    correct_answer = is_prime(number)
    return 'yes' if correct_answer else 'no'


def is_prime(number: int) -> bool:
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    limit = int(number ** 0.5) + 1
    for i in range(3, limit, 2):
        if number % i == 0:
            return False
    return True


def get_question():
    number = random.randint(0, 100)
    return number, check_answer(number) 


if __name__ == "__main__":
    main()