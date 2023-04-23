def calculate_result(score):
    counter = 0
    rounds = score.split("|")
    scores = translate_score(rounds)
    index = 0
    try:
        for i in range(10):
            if is_strike(index, scores):
                counter += (10 + calculate_strike(scores, index))
            elif is_spare(index, scores):
                counter += (10 + calculate_spare(scores, index))
            else:
                counter += (scores[index] + scores[index+1])
            index += 2
        return counter
    except IndexError:
        return counter


def is_strike(i, scores) -> int:
    return scores[i] == 10


def is_spare(i, scores):
    return scores[i] + scores[i+1] == 10


def calculate_strike(rounds, i):
    if rounds[i+2] == 10:
        return rounds[i+2] + rounds[i+4]
    return rounds[i+2] + rounds[i+3]


def calculate_spare(rounds, i):
    return rounds[i+2]


def translate_score(rounds):
    scores = []
    tmp = 0
    rounds = "".join(rounds)
    for i, throw in enumerate(rounds):
        if "X" in throw:
            scores.append(10)
            scores.append(0)
        elif "/" in throw:
            scores.append(10 - tmp)
        elif "-" in throw:
            scores.append(0)
        else:
            scores.append(int(throw))
            tmp = int(throw)

    return scores


def is_full_match(rounds):
    return len(rounds.split("|")) == 10
