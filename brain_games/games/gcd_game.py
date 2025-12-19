import secrets
import math


RULES = "Find the greatest common divisor of given numbers."


def get_question():
    first = secrets.randbelow(101)
    second = secrets.randbelow(101)
    return str(f"{first} {second}"), math.gcd(int(first), int(second))
