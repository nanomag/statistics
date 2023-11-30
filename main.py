from typing import Dict, List


class DataCapture:
    def __init__(self) -> None:
        """
        Initializes a DataCapture object.

        Attributes:
            numbers (List[int]): A list to store numbers.
            counter (Dict[int, int]): A dictionary to count occurrences of each number.
        """
        self.numbers: List[int] = []
        self.counter: Dict[int, int] = {}

    def add(self, number: int) -> None:
        """
        Adds a number to the DataCapture object and updates the counter.

        Parameters:
            number (int): The number to be added.
        """
        self.numbers.append(number)
        self.counter[number] = self.counter.get(number, 0) + 1

    def build_stats(self) -> "Stats":
        """
        Builds and returns a Stats object based on the data in the DataCapture object.

        Returns:
            Stats: A Stats object containing statistics about the stored numbers.
        """
        return Stats(self.numbers, self.counter)


class Stats:
    def __init__(self, numbers: List[int], counter: Dict[int, int]) -> None:
        """
        Initializes a Stats object with the provided numbers and counter.

        Parameters:
            numbers (List[int]): A list of numbers.
            counter (Dict[int, int]): A dictionary representing the count of each number.
        """
        self.numbers = numbers
        self.counter = counter

    def less(self, number: int) -> int:
        """
        Calcuates the count of numbers less than "number" and returns the count.

        Parameters:
            number (int): The threshold value.

        Returns:
            int: The count of numbers less than "number".
        """
        return sum(self.counter[num] for num in self.counter if num < number)

    def between(self, min_number: int, max_number: int) -> int:
        """
        Calculates the count of numbers between min_number (inclusive) and max_number (inclusive) and returns the count.

        Parameters:
            min_number (int): The lower threshold value.
            max_number (int): The upper threshold value.

        Returns:
            int: The count of numbers between min_number (inclusive) and max_number (inclusive).
        """
        return sum(
            self.counter[num] for num in self.counter if min_number <= num <= max_number
        )

    def greater(self, number: int) -> int:
        """
        Calculates the count of numbers greater than "number" and returns the count.

        Parameters:
            number (int): The threshold value.

        Returns:
            int: The count of numbers greater than "number".
        """
        return sum(self.counter[num] for num in self.counter if num > number)
