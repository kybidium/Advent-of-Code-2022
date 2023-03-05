f = open("input4.txt")
f_read = f.read()

def fully_contained(ID_lst):
    tally = 0
    for line in ID_lst.strip().split("\n"):
        broken = False
        first, second = line.split(",")
        first1, first2 = first.split("-")
        second1, second2 = second.split("-")
        range1 = list(range(int(first1), int(first2) + 1))
        range2 = list(range(int(second1), int(second2) + 1))
        for n in range((min(len(range1), len(range2)))):
            if not (range2[n] in range1 or range1[n] in range2):
                broken = True
                break
        if broken == True:
            broken = False
            continue
        tally += 1
    return tally

print(fully_contained(f_read))
f.close()