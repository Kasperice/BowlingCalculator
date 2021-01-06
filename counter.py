def calculate_result(score):
    counter = 0
    last = False
    rounds = score.split("|")
    print(rounds)
    for i, round in enumerate(rounds):
        if i == 9:
            print("AAA")
            last = True
        if "X" in round:
            counter += calculate_strike(rounds, i, last=last)
        elif "/" in round:
            counter += calculate_spare(rounds, i, last=last)
        elif "-" in round:
            counter += int(round.replace("-", ""))
        elif len(round) == 1:
            counter += int(round[0])
        else:
            counter += (int(round[0]) + int(round[1]))

    print(counter)
    return counter


def calculate_strike(rounds, i, last):
    if last:
        return 10 + rounds[i+1]
    return 0


def calculate_spare(rounds, i, last):
    return 0
