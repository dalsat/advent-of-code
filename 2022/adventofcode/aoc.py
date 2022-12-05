from typing import Any


def load_day(day: int, separator="\n"):
    with open(f"input/day-{str(day).zfill(2)}.txt", "r") as f:
        data: Any = f.read()

    if separator:
        data = [line for line in data.split(separator) if line]
    return data
