from typing import Dict, List, Tuple


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
        (
            self.less_counter,
            self.between_counter,
            self.greater_counter,
        ) = self._calculate_counters()

    def less(self, number: int) -> int:
        """
        Returns the count of numbers less than "number" and returns the count.

        Parameters:
            number (int): The threshold value.

        Returns:
            int: The count of numbers less than "number".
        """
        return self.less_counter.get(number, 0)

    def between(self, min_number: int, max_number: int) -> int:
        """
        Calculates the count of numbers between min_number (inclusive) and max_number (inclusive) and returns the count.

        Parameters:
            min_number (int): The lower threshold value.
            max_number (int): The upper threshold value.

        Returns:
            int: The count of numbers between min_number (inclusive) and max_number (inclusive).
        """
        return (
            self.between_counter.get(max_number, 0)
            - self.between_counter.get(min_number, 0)
            + self.counter.get(min_number, 0)
        )

    def greater(self, number: int) -> int:
        """
        Calculates the count of numbers greater than "number" and returns the count.

        Parameters:
            number (int): The threshold value.

        Returns:
            int: The count of numbers greater than "number".
        """
        return self.greater_counter.get(number, 0)

    def _calculate_counters(
        self
    ) -> Tuple[Dict[int, int], Dict[int, int], Dict[int, int]]:
        """
        Calculates cumulative counters for less, between, and greater.

        Returns:
            Tuple[Dict[int, int], Dict[int, int], Dict[int, int]]: A tuple containing less_counter,
            between_counter, and greater_counter.
        """
        less_counter, between_counter, greater_counter = {}, {}, {}
        cumulative_less, cumulative_greater = 0, 0

        # Iterate through sorted numbers
        for num in sorted(self.counter):
            # Calculate cumulative count for less_counter
            cumulative_less += self.counter[num]
            less_counter[num] = cumulative_less

            # Calculate cumulative count for greater_counter
            cumulative_greater += self.counter[num]
            greater_counter[num] = cumulative_greater

            # Calculate cumulative count for between_counter
            between_counter[num] = cumulative_less

        return less_counter, between_counter, greater_counter
