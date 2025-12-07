import secrets
import math


def main():
    print("Welcome to the Brain Games!")


MAX_TRIES = 3
RULES = "Find the greatest common divisor of given numbers."


def get_question():
    first = secrets.randbelow(101)
    second = secrets.randbelow(101)
    return str(f"{first} {second}"), math.gcd(int(first), int(second))


if __name__ == "__main__":
    main()