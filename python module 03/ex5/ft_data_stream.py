#! /usr/bin/env python3
import random
import typing

PLAYERS = ['alice', 'charlie', 'bob', 'dylan']
ACTIONS = ['run', 'eat', 'sleep', 'grab', 'climb', 'move', 'swim', 'release']

# is infinity, the number of loops is define on the main


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        player = random.choice(PLAYERS)
        action = random.choice(ACTIONS)
        yield (player, action)


def consume_event(
        event_list: list[tuple[str, str]]
) -> typing.Generator[tuple[str, str], None, None]:
    while len(event_list) > 0:
        event = random.choice(event_list)
        event_list.remove(event)
        yield event


def main():
    start = 0
    g = gen_event()
    while start < 1000:
        event = next(g)
        print(f"Event {start}: Player {event[0]} did action {event[1]}")
        start += 1
    event_list = []
    h = gen_event()
    while len(event_list) < 10:
        event = next(h)
        event_list.append(event)
    print(f"Built list of 10 event: {event_list}")
    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    main()
