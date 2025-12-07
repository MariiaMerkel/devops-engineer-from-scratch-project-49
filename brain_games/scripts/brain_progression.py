from brain_games.games.progression_game import MAX_TRIES, RULES, get_question
from brain_games.engine import game_engine


def main():
    game_engine(rules=RULES, max_tries=MAX_TRIES, func_question=get_question)


if __name__ == "__main__":
    main()