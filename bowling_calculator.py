import collections
from counter import calculate_result
from display import display_leaderboard

Player = collections.namedtuple('Player', "name scores current_result")


def prepare_lanes(number_of_lanes):
    lanes = []
    for i in range(number_of_lanes):
        lanes.append(f"lane{i+1}")
    return lanes


players = []
number_of_lanes = 3

lanes = prepare_lanes(number_of_lanes)
for lane in lanes:
    try:
        with open(f"{lane}.txt") as file:
            players.clear()
            for line in file:
                line = line.replace("\n", "")
                (name, score) = line.split(":")
                players.append(Player(name, score, calculate_result(score)))
            print("*"*40)
            display_leaderboard(lane, players)
    except EnvironmentError:
        print(f"{lane} is not used")



