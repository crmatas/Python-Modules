#! /usr/bin/env python3
import sys


def main():
    print("=== Player Score Analytics ===")
    scores = []
    for arg in (sys.argv[1:]):
        try:
            number = int(arg)
            scores.append(number)
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
    if len(scores) == 0:
        print(f"No scores provided. Usage: "
              f"{sys.argv[0]} <score1> <score2> ...")
        return
    print(f"Scores processed: {scores}")
    players = len(scores)
    print(f"Total players: {players}")
    total_scores = sum(scores)
    print(f"Total score: {total_scores}")
    max_scores = max(scores)
    min_scores = min(scores)
    average_score = total_scores / players
    range_score = max_scores - min_scores
    print(f"Average score: {average_score}")
    print(f"Hight score: {max_scores}")
    print(f"Low score: {min_scores}")
    print(f"Score range: {range_score}")


if __name__ == "__main__":
    main()
