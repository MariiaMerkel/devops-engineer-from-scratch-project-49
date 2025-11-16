import prompt
import random
from brain_games.cli import welcome_user
from typing import Callable


def game_engine (rules: str, max_tries: int, func_question: Callable, check_answer: Callable):
	name, age = welcome_user()
	print(f"Game rules: {rules}")
	win = False
	count_tries = 0

	while count_tries < max_tries:
		question = func_question()
		print(f"Your question is: {question}")
		answer = prompt.string(f'Input your answer: ')
		check = check_answer(question, answer)
		if check:
			count_tries += 1
		else:
			print(f"Sorry, {name}! Answer [{answer}] is not right for [{question}].\nTry again!")
			count_tries = 0
	print(f"Congratulations {name}! You win!")