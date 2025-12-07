import random
import math


def main():
    print("Welcome to the Brain Games!")


MAX_TRIES = 3
RULES = "Find the greatest common divisor of given numbers."

def get_question():
    first = random.randint(1, 100)
    second = random.randint(1, 100)
    return str(f"{first} {second}"), math.gcd(int(first), int(second))

if __name__ == "__main__":
    main()