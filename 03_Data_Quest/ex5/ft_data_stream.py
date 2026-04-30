#!/usr/bin/env python3

"""Filename : ft_data_stream.py

Date: 2026-03-23
Description: This program introduce to generators and yield keyworld
to create memory-efficient data streams. Generator can produce values
on-demand rather than storing everything in memory.
"""
from collections.abc import Generator
import random


EVENT_TYPES = ["fight a monster", "search a treasure", "sleep",
               "eat", "run", "grap", "open a door", "climb",
               "move", "swim", "explore the room"]


PLAYER_NAMES = ["alice", "bob", "charlie", "dylan", "jolyne",
                "camille", "ady", "emma", "luka", "audrey"]


def gen_event() -> Generator[tuple[str, str]]:
    """Function to generate random event in EVENT_TYPES for a random
    player in PLAYER_NAMES
    """
    number_event: int = len(EVENT_TYPES)
    number_player: int = len(PLAYER_NAMES)
    for _ in PLAYER_NAMES:
        name: str = PLAYER_NAMES[random.randint(0, number_player - 1)]
    for _ in EVENT_TYPES:
        event: str = EVENT_TYPES[random.randint(0, number_event - 1)]
    event_generated: tuple[str, str] = (name, event)
    yield event_generated


def consume_event(list_event: list[tuple[str, str]]) -> \
                  Generator[list[tuple[str, str]]]:
    """Function to generate a random deletion in a list of events and
    yield the remaining list
    """
    number_of_event: int = len(list_event)
    index: int = random.randint(0, number_of_event - 1)
    print(f"Got event from list: {list_event[index]}")
    del list_event[index]
    yield list_event


def main() -> None:
    """Entry point of the program"""
    print("=== Game Data Stream Processor ===")
    for i in range(1000):
        event = next(gen_event())
        print(f"Event {i}: Player {event[0]} did action {event[1]}")
    list_events: list[tuple[str, str]] = []
    index: int = 0
    for i in range(10):
        list_events.append(next(gen_event()))
        index += 1
    print(f"Build list of 10 events: {list_events}")
    for i in range(10):
        new_list = next(consume_event(list_events))
        print(f"Remains in list : {new_list}")


if __name__ == "__main__":
    main()
