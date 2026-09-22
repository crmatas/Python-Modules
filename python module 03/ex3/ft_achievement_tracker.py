#! /usr/bin/env python3
import random

# list with all posible achievements

ACHIVEMENTS = ['Crafting Genius', 'World Savior', 'Master Explorer',
               'Collector Supreme', 'Untouchable', 'Boss Slayer',
               'Treasure Hunter', 'Unstopable', 'Strategist', 'Speed Runner',
               'Sharp Mind', 'First Steps', 'Hidden Path Finder']


def gen_player_achievements() -> set:
    num_achievements = random.randint(5, 9)
    chosen = random.sample(ACHIVEMENTS, num_achievements)
    return set(chosen)


if __name__ == "__main__":
    # dic of players
    players = {
        'Alice': gen_player_achievements(),
        'Bob': gen_player_achievements(),
        'Charlie': gen_player_achievements(),
        'Dylan': gen_player_achievements()
    }
    print("=== Achievement Tracker System ===")
    print("")
    for name, ach in players.items():
        print(f"Player {name}: {ach}")
    print("")
    all_distint = players['Alice'].union(
        players['Bob'],
        players['Charlie'],
        players['Dylan']
    )
    print(f"All achievements: {all_distint}")
    print("")
    common = players['Alice'].intersection(
        players['Bob'],
        players['Charlie'],
        players['Dylan']
    )
    print(f"Common achievements: {common}")
    print("")
    for name, ach in players.items():
        others_achievement: set[str] = set()
        for other_name, other_ach in players.items():
            if other_name != name:
                others_achievement = others_achievement.union(other_ach)
        only_this_player = ach.difference(others_achievement)
        print(f"Only {name} has: {only_this_player}")
    print("")
    master_set = set(ACHIVEMENTS)
    for name, ach in players.items():
        missing = master_set.difference(ach)
        print(f"{name} is missing: {missing}")
