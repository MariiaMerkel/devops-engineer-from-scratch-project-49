import secrets


RULES = "What number is missing in the progression?"


def get_question():
    first = secrets.randbelow(11)
    step = secrets.randbelow(11)
    skip = secrets.randbelow(10)
    progressive = [first + step * i for i in range(10)]
    right_answer = progressive[skip]
    progressive[skip] = '..'
    return str(' '.join(str(x) for x in progressive)), right_answer
