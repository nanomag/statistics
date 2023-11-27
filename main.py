from typing import Dict, List


class DataCapture:
    def __init__(self) -> None:
        self.numbers: List[int] = []
        self.counter: Dict[int, int] = {}

    def add(self, number: int) -> None:
        self.numbers.append(number)
        self.counter[number] = self.counter.get(number, 0) + 1

    def build_stats(self) -> "Stats":
        return Stats(self.numbers, self.counter)


class Stats:
    def __init__(self, numbers: List[int], counter: Dict[int, int]) -> None:
        self.numbers = numbers
        self.counter = counter

    def less(self, a: int) -> int:
        return sum(self.counter[num] for num in self.counter if num < a)

    def between(self, a: int, b: int) -> int:
        return sum(self.counter[num] for num in self.counter if a <= num <= b)

    def greater(self, a: int) -> int:
        return sum(self.counter[num] for num in self.counter if num > a)
