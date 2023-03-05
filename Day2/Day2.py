f = open("input2.txt")
f_read = f.read()

def rock_paper_scissors_calculator(strat):
    dict_A = {
        "X": 3
        "Y": 0
        "Z": 6
    }
    dict_B = {
        "X": 0
        "Y": 3
        "Z": 6
    }
    dict_C = {
        "X": 6
        "Y": 0
        "Z": 3
    }
    dict_gen  = {
        "A": dict_A
        "B": dict_B
        "C": dict_C
    }

    # format is letterspaceletterspacenewline
    for round in strat.split("\n"):
        # is there a better way to process the file?
        

f.close()