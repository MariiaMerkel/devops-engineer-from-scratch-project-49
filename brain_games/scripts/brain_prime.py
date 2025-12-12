from brain_games.games.prime_game import RULES, get_question
from brain_games.engine import game_engine


def main():
    game_engine(rules=RULES, func_question=get_question)


if __name__ == "__main__":
    main()