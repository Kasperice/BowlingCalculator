import unittest
from counter import translate_score, is_strike, is_spare, calculate_spare, calculate_strike, is_full_match, calculate_result


class TestCounter(unittest.TestCase):
    def test_score_translation(self):
        results = ['12', '45', '5/', '8-', '9/', 'X', 'X', 'X', 'X', 'X']
        actual = translate_score(results)
        expected = [1, 2, 4, 5, 5, 5, 8, 0, 9, 1, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0]
        self.assertEqual(actual, expected)

    def test_is_not_strike(self):
        scores = [2]
        actual = is_strike(0, scores)
        self.assertEqual(actual, False)

    def test_is_strike(self):
        scores = [10]
        actual = is_strike(0, scores)
        self.assertEqual(actual, True)

    def test_is_not_spare(self):
        scores = [2, 2]
        actual = is_spare(0, scores)
        self.assertEqual(actual, False)

    def test_is_spare(self):
        scores = [2, 8]
        actual = is_spare(0, scores)
        self.assertEqual(actual, True)

    def test_calculate_spare(self):
        scores = [2, 8, 2]
        actual = calculate_spare(scores, 0)
        expected = 2
        self.assertEqual(actual, expected)

    def test_calculate_strike(self):
        scores = [10, 0, 5, 4]
        actual = calculate_strike(scores, 0)
        expected = 9
        self.assertEqual(actual, expected)

    def test_calculate_two_strikes(self):
        scores = [10, 0, 10, 0, 4, 4]
        actual = calculate_strike(scores, 0)
        expected = 14
        self.assertEqual(actual, expected)

    def test_is_full_match(self):
        rounds = "9-|9-|9-|9-|9-|9-|9-|9-|9-|9-"
        actual = is_full_match(rounds)
        self.assertEqual(actual, True)

    def test_is_not_full_match(self):
        rounds = "9-|9-|9-|9-|9-|9-|9-"
        actual = is_full_match(rounds)
        self.assertEqual(actual, False)

    def test_calculate_result_for_two_rounds(self):
        rounds = "11|11"
        actual = calculate_result(rounds)
        self.assertEqual(actual, 4)

    def test_calculate_result_for_full_match_with_spares(self):
        rounds = "9/|9/|9/|9/|9/|9/|9/"
        actual = calculate_result(rounds)
        self.assertEqual(actual, 114)

    def test_calculate_result_for_full_match_with_strikes(self):
        rounds = "X|X|X|X|X|X|X|X|X|X|XX"
        actual = calculate_result(rounds)
        self.assertEqual(actual, 300)

    def test_calculate_result_for_full_match_with_strikes_and_spares(self):
        rounds = "12|45|5/|8-|9/|X|X|X|X|X"
        actual = calculate_result(rounds)
        self.assertEqual(actual, 148)


if __name__ == '__main__':
    unittest.main()
