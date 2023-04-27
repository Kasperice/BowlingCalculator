import pytest

from bowling_calculator.counter import (
    translate_score,
    is_strike,
    is_spare,
    calculate_spare,
    calculate_strike,
    is_full_match,
    calculate_result,
)


@pytest.mark.parametrize(
    "score, translated_score",
    [
        ("12", [1, 2]),
        ("5/", [5, 5]),
        ("8-", [8, 0]),
        ("9/", [9, 1]),
        ("X", [10, 0]),
        (
            ["12", "45", "5/", "8-", "9/", "X", "X", "X", "X", "X"],
            [1, 2, 4, 5, 5, 5, 8, 0, 9, 1, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0],
        ),
    ],
)
def test_score_translation(score, translated_score):
    actual = translate_score(score)
    assert actual == translated_score


@pytest.mark.parametrize("score, expected", [([2], False), ([10], True)])
def test_is_strike(score, expected):
    actual = is_strike(0, score)
    assert actual == expected


@pytest.mark.parametrize("score, expected", [([2, 2], False), ([2, 8], True)])
def test_is_spare(score, expected):
    actual = is_spare(0, score)
    assert actual == expected


def test_calculate_spare():
    scores = [2, 8, 2]
    actual = calculate_spare(scores, 0)
    expected = 2
    assert actual == expected


def test_calculate_strike():
    scores = [10, 0, 5, 4]
    actual = calculate_strike(scores, 0)
    expected = 9
    assert actual == expected


def test_calculate_two_strikes():
    scores = [10, 0, 10, 0, 4, 4]
    actual = calculate_strike(scores, 0)
    expected = 14
    assert actual == expected


@pytest.mark.parametrize(
    "score, expected",
    [("9-|9-|9-|9-|9-|9-|9-|9-|9-|9-", True), ("9-|9-|9-|9-|9-|9-|9-", False)],
)
def test_is_full_match(score, expected):
    actual = is_full_match(score)
    assert actual == expected


@pytest.mark.parametrize(
    "score, result",
    [
        ("11|11", 4),
        ("9/|9/|9/|9/|9/|9/|9/", 114),
        ("X|X|X|X|X|X|X|X|X|X|XX", 300),
        ("12|45|5/|8-|9/|X|X|X|X|X", 148),
        ("--|--", 0),
    ],
)
def test_calculate_result(score, result):
    actual = calculate_result(score)
    assert actual == result
