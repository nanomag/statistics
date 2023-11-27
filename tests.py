import unittest

from main import DataCapture


class TestStats(unittest.TestCase):
    def test_less(self):
        capture = DataCapture()
        capture.add(3)
        capture.add(9)
        capture.add(3)
        capture.add(4)
        capture.add(6)

        stats = capture.build_stats()
        self.assertEqual(stats.less(4), 2)

    def test_between(self):
        capture = DataCapture()
        capture.add(3)
        capture.add(9)
        capture.add(3)
        capture.add(4)
        capture.add(6)

        stats = capture.build_stats()
        self.assertEqual(stats.between(3, 6), 4)

    def test_greater(self):
        capture = DataCapture()
        capture.add(3)
        capture.add(9)
        capture.add(3)
        capture.add(4)
        capture.add(6)

        stats = capture.build_stats()
        self.assertEqual(stats.greater(4), 2)


if __name__ == "__main__":
    unittest.main()
