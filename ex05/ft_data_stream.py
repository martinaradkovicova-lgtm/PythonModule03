import random
from typing import Generator


def gen_event() -> Generator[tuple[str, str], None, None]:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = [
      "run",
      "eat",
      "sleep",
      "grab",
      "move",
      "climb",
      "use",
      "swim",
      "release",
    ]

    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(
    event_list: list[tuple[str, str]],
) -> Generator[tuple[str, str], None, None]:
    while event_list:
        idx = random.randrange(len(event_list))
        item = event_list.pop(idx)
        yield item


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")

    stream = gen_event()

    for i in range(1000):
        event = next(stream)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")

    ten_events = []
    for _ in range(10):
        ten_events.append(next(stream))

    print(f"Built list of 10 events: {ten_events}")

    for event in consume_event(ten_events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {ten_events}")
