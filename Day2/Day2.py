"""
Resources Consulted: None
"""
# Code Works

f = open("input2.txt")
f_read = f.read().strip()

def rock_paper_scissors_calculator(strat):
    """
    Determines a rock paper scissors player's score based on a strategy outlined
    with rows "<opponent choice> <player choice>" where X, Y, and Z represent
    the player choice of rock, paper, and scissors and A, B, and C represent the
    opponent's choice of rock, paper, and scissors respectively.

    Arg:
        strat: the stategy formatted in the above rows (string)

    Returns: score: the player's total score (int)
    """
    # generates a nested dictionary containing the rock paper scissors strategies
    dict_A = {
        "X": 3,
        "Y": 6,
        "Z": 0,
    }
    dict_B = {
        "X": 0,
        "Y": 3,
        "Z": 6,
    }
    dict_C = {
        "X": 6,
        "Y": 0,
        "Z": 3,
    }
    dict_gen  = {
        "A": dict_A,
        "B": dict_B,
        "C": dict_C,
        "X": 1,
        "Y": 2,
        "Z": 3,
    }

    score = 0
    # iterates through each round's strategy
    for round in strat.split("\n"):
        # adds the choice score and the win score
        gain = int(dict_gen[round[0]][round[2]]) + int(dict_gen[round[2]])
        # adds the result to the total score
        score += gain

    return score

def rock_paper_scissors_calc_2(strat):
    """
    Determines a rock paper scissors player's score based on a strategy outlined
    with rows "<opponent choice> <player choice>" where X, Y, and Z represent
    whether the player chooses to win, lose, or draw and A, B, and C represent the
    opponent's choice of rock, paper, and scissors respectively.

    Arg:
        strat: the stategy formatted in the above rows (string)

    Returns: score: the player's total score (int)
    """
    # generates a nested dictionary containing the part 2 strategies
    dict_A = {
        "X": 3,
        "Y": 1,
        "Z": 2,
    }
    dict_B = {
        "X": 1,
        "Y": 2,
        "Z": 3,
    }
    dict_C = {
        "X": 2,
        "Y": 3,
        "Z": 1,
    }
    dict_gen  = {
        "A": dict_A,
        "B": dict_B,
        "C": dict_C,
        "X": 0,
        "Y": 3,
        "Z": 6,
    }

    score = 0
    # iterates through each round's strategy
    for round in strat.split("\n"):
        # adds the win score and the choice score
        gain = int(dict_gen[round[0]][round[2]]) + int(dict_gen[round[2]])
        # adds the result to the total score
        score += gain

    return score

# prints result of each function with the input given
print(rock_paper_scissors_calculator(f_read))
print(rock_paper_scissors_calc_2(f_read))
f.close()
