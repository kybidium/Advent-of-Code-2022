f = open("input2.txt")
f_read = f.read().strip()
def rock_paper_scissors_calculator(strat):
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
    # format is letterspaceletterspacenewline
    score = 0
    for round in strat.split("\n"):
        # is there a better way to process the file?
        gain = int(dict_gen[round[0]][round[2]]) + int(dict_gen[round[2]])
        score += gain

    return score

print(rock_paper_scissors_calculator(f_read))
f.close()
