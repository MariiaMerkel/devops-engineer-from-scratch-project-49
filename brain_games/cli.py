import prompt


def welcome_user():
    name = prompt.string("What is your name? ")
    age = prompt.integer("How old are you? ")
    print(f"Hello, {name}! You are {age} years old.")
    return name, age
