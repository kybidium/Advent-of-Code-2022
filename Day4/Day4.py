f = open("input4.txt")
f_read = f.read()

def fully_contained(ID_lst):
    tally = 0
    for line in fully_contained.split("\n"):
        first, second = line.split(",")
        first1, first2 = first.split("-")
        second1, second2 = second.split("-")
        range1 = list(range(int(first1), int(first2) + 1))
        range2 = list(range(int(second1), int(second2) + 1))
        if range1 in range2 or range2 in range1:
            tally += 1
    return tally

print(fully_contained(f_read))
f.close()