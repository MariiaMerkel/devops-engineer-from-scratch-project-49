from brain_games.games.progression_game import MAX_TRIES, RULES, get_question, check_answer
from brain_games.engine import game_engine

def main():
    game_engine(rules=RULES, max_tries = MAX_TRIES, func_question=get_question, check_answer=check_answer)

if __name__ == "__main__":
    main()