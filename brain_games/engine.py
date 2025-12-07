import prompt
from brain_games.cli import welcome_user
from typing import Callable


def game_engine(rules: str, max_tries: int, func_question: Callable):
	name = welcome_user()
	print(f"Game rules: {rules}")
	count_tries = 0

	while count_tries < max_tries:
		question, correct_answer = func_question()
		print(f"Question: {question}")
		answer = prompt.string('Your answer: ')
		check = str(answer) == str(correct_answer)
		if check:
			print("Correct!")
			count_tries += 1
		else:
			print(
				f"'{answer}' is wrong answer ;(. "
				f"Correct answer was '{correct_answer}'.\n"
				f"Let's try again, {name}!"
)
			break
		if count_tries == max_tries:
			print(f"Congratulations, {name}! You win!")