import pytest

from main import DataCapture


def test_capture_valid_numbers():
    capture = DataCapture()
    capture.add(1)
    capture.add(2)
    capture.add(3)
    assert len(capture.numbers) == 3


def test_capture_valid_string_numbers():
    capture = DataCapture()
    capture.add(1)
    capture.add("2")
    capture.add("3")
    assert len(capture.numbers) == 3


def test_capture_negative_number():
    capture = DataCapture()
    capture.add(1)
    capture.add(2)

    with pytest.raises(
        ValueError,
        match="Invalid input: -1. Please enter a positive integer less than 1000.",
    ):
        capture.add(-1)


def test_capture_large_number():
    capture = DataCapture()
    with pytest.raises(
        ValueError,
        match="Invalid input: 1500. Please enter a positive integer less than 1000.",
    ):
        capture.add(1500)


def test_capture_invalid_string():
    capture = DataCapture()
    capture.add(1)
    capture.add(2)

    with pytest.raises(
        ValueError,
        match="Invalid input: wrong. Please enter a positive integer less than 1000.",
    ):
        capture.add("wrong")


@pytest.fixture
def data_capture():
    capture = DataCapture()
    capture.add(3)
    capture.add(9)
    capture.add(3)
    capture.add(4)
    capture.add(6)

    return capture


def test_less(data_capture):
    stats = data_capture.build_stats()
    assert stats.less(4) == 2


def test_between(data_capture):
    stats = data_capture.build_stats()
    assert stats.between(3, 6) == 4


def test_greater(data_capture):
    stats = data_capture.build_stats()
    assert stats.greater(4) == 2
