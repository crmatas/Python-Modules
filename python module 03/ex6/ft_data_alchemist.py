#! /usr/bin/env python3
import random
PLAYERS = [
    'Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory',
    'john', 'kevin', 'Liam'
]


def main():
    print(f"Initial list of players: {PLAYERS}")
    names_cap = [n.capitalize() for n in PLAYERS]
    print(f"New list with all names capitalized: {names_cap}")
    names_upper = [n for n in PLAYERS if n[0].isupper()]
    print(f"New list of capitalized names only: {names_upper}")
    print("")
    score_dic = {player: random.randint(1, 1000) for player in names_upper}
    print(f"Score dict: {score_dic}")
    total_scores = sum(score_dic.values())
    average = total_scores / len(names_upper)
    print(f"Score average is {average:.2f}")
    highest_dict = {player: score for player,
                    score in score_dic.items() if score > average}
    print(f"High scores {highest_dict}")


if __name__ == "__main__":
    print("=== Game Data Alchemist ===")
    print("")
    main()
