import prompt
import random


def main():
	print("Welcome to the Brain Games!")

WORDS = (
	"python", 
	"java"
)

MAX_TRIES = 3
RULES = "Input anagram of word."

def check_answer(question: str, answer: str) -> bool:
	return sorted(answer) == sorted(question) and answer != question

def get_question():
	question = random.choice(WORDS)

def welcome_user():
	name = prompt.string("What is your name?")
	age = prompt.integer("How old are you?")
	print(f"Hello, {name}! You are {are} years old.")
	return name, age

def brain_game():
	name, age = welcome_user()
	print(f"Game rules: "{RULES})
	win = False
	count_tries = 0

	while count_tries < MAX_TRIES:
		question = get_question()
		print(f"Your question is: {random.choice(WORDS)}")
		answer = prompt.string(f'Input your answer: {question}')
		check = check_answer(question, answer)
		if check:
			count_tries += 1
		else:
			print(f"Sorry, {name}! Answer [{answer}] is not right for [{question}].\nTry again!")
			count_tries = 0
	print(f"Congratulations {name}! You win!")


if __name__ == "__main__":
	main()
