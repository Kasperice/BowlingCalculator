from unittest.mock import patch
from io import StringIO

from bowling_calculator.display import display_leaderboard, unpack_tuple
from bowling_calculator.player import Player


def test_unpack_tuple():
    test_player = Player('John', ['12', '45', '5/', '8-', '9/', 'X', 'X', 'X', 'X', 'X'], 56)
    assert unpack_tuple(test_player) == ('John', ['12', '45', '5/', '8-', '9/', 'X', 'X', 'X', 'X', 'X'], 56)


def test_display_leaderboard():
    lane = "lane1"
    players = [Player(name='Jane', scores='12|45|5/|8-|9/|X|X|X|X|X', current_result=148),
               Player(name='John', scores='9-|9-|9-|9-|9-|9-|9-|9-|9-', current_result=81)]
    with patch('sys.stdout', new=StringIO()) as patched_out:
        display_leaderboard(lane, players)
        assert patched_out.getvalue().replace('\n', '') == "lane1The current leader is: JaneLeaderboard:Jane 12|45|5/|8-|9/|X|X|X|X|X 148John 9-|9-|9-|9-|9-|9-|9-|9-|9- 81Game is not finished yet, keep going!"


