"""
Resources Consulted:
    https://techbeamers.com/program-python-list-contains-elements/
    https://www.w3schools.com/python/ref_set_intersection.asp
    https://favtutor.com/blogs/set-intersection-python#:~:text=Difference%20betw
        een%20set%20intersection(),structure%20to%20find%20the%20intersection.
"""
# Code Works

f = open("input4.txt")
f_read = f.read()

def fully_contained(ID_lst):
    tally = 0
    for line in ID_lst.strip().split("\n"):
        first, second = line.split(",")
        first1, first2 = first.split("-")
        second1, second2 = second.split("-")
        range1 = set(range(int(first1), int(first2) + 1))
        range2 = set(range(int(second1), int(second2) + 1))
        if (range1 & range2 == range1) or (range1 & range2 == range2):
            tally += 1

    return tally

def overlaps(ID_lst):
    tally = 0
    for line in ID_lst.strip().split("\n"):
        first, second = line.split(",")
        first1, first2 = first.split("-")
        second1, second2 = second.split("-")
        range1 = set(range(int(first1), int(first2) + 1))
        range2 = set(range(int(second1), int(second2) + 1))
        if range1 & range2:
            tally += 1

    return tally

print(fully_contained(f_read))
print(overlaps(f_read))
f.close()
