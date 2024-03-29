from operator import attrgetter

from bowling_calculator.counter import is_full_match


def display_leaderboard(lane, players) -> None:
    players = sorted(players, key=attrgetter("current_result"), reverse=True)
    print(f"{lane}")
    print(f"The current leader is: {getattr(players[0], 'name')}\nLeaderboard:")
    for player in players:
        name, scores, result = unpack_tuple(player)
        print(name, scores, result)

    if is_full_match(scores):
        print(f"\nGame is finished, congratulations {getattr(players[0], 'name')}\n")
    else:
        print("\nGame is not finished yet, keep going!\n")


def unpack_tuple(player):
    name = getattr(player, "name")
    scores = getattr(player, "scores")
    result = getattr(player, "current_result")
    return name, scores, result
