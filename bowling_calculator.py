from bowling_calculator.counter import calculate_result
from bowling_calculator.display import display_leaderboard
from bowling_calculator.player import Player


players = []
number_of_lanes = 3


def main():
    lanes = [f"lane{i+1}" for i in range(number_of_lanes)]
    for lane in lanes:
        try:
            with open(f"{lane}.txt") as file:
                players.clear()
                for line in file:
                    line = line.replace("\n", "")
                    (name, score) = line.split(":")
                    players.append(Player(name, score, calculate_result(score)))
                print("*" * 40)
                display_leaderboard(lane, players)
        except EnvironmentError:
            print(f"{lane} is not used")


if __name__ == "__main__":
    main()
