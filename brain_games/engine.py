import prompt
from brain_games.cli import welcome_user

MAX_TRIES = 3


def game_engine(game: object):
	name = welcome_user()
	print(f"Game rules: {game.RULES}")

	for tries in range(MAX_TRIES):
		question, correct_answer = game.get_question()
		print(f"Question: {question}")
		answer = prompt.string('Your answer: ')
		if str(answer) == str(correct_answer):
			print("Correct!")
		else:
			print(
				f"'{answer}' is wrong answer ;(. "
				f"Correct answer was '{correct_answer}'.\n"
				f"Let's try again, {name}!"
			)
			break
	else:
		print(f"Congratulations, {name}! You win!")
