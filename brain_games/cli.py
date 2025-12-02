import prompt


def welcome_user():
    name = prompt.string("May I have your name?")
    city = prompt.string("Where are you from?")
    print(f"Hello, {name} from {city} !")
    return name, city
