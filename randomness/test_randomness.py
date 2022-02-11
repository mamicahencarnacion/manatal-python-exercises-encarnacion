import unittest

from randomness import get_lottery_output


class TestLotteryOutput(unittest.TestCase):
    def test_is_output_list(self):
        output = get_lottery_output()
        self.assertIsInstance(output, list)

    def test_no_repeating_number(self):
        output = get_lottery_output()
        self.assertEqual(len(output), len(set(output)))

    def test_is_sorted(self):
        output = get_lottery_output()

        self.assertEqual(output, sorted(output))

    def test_is_between_one_fifty(self):
        output = get_lottery_output()
        for number in output:
            self.assertIn(number, range(1, 51))


if __name__ == "__main__":
    unittest.main()
