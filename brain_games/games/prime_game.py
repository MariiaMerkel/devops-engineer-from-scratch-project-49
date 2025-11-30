import random


def main():
    print("Welcome to the Brain Games!")


MAX_TRIES = 3
RULES = "Input 'yes' if this number is prime and 'no' if it is not prime"


def check_answer(question: str, answer: str) -> bool:
    question = int(question)
    right_answer = is_prime(question)
    
    return (right_answer and answer == 'yes') or (not right_answer and answer == 'no')

def is_prime(number:int) -> bool:
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
    return random.randint(0, 100)

if __name__ == "__main__":
    main()