import random
import math


def main():
    print("Welcome to the Brain Games!")


OPERATORS = ('+', '-', '*', '/', '%')

MAX_TRIES = 3
RULES = "Calculate the greatest common divided and input result."

def get_question():
    first = random.randint(1, 100)
    second = random.randint(1, 100)
    return str(f"{first} {second}"), math.gcd(int(first), int(second))

if __name__ == "__main__":
    main()