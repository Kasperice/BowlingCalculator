import collections
from counter import calculate_result

Player = collections.namedtuple('Player', ['name', 'scores', 'current_result'])

players = []
with open("lane1.txt") as file:
    for line in file:
        line = line.replace("\n", "")
        (name, score) = line.split(":")
        players.append(Player(name, score, calculate_result(score)))


