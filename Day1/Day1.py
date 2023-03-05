"""
Resources Consulted:
    https://www.freecodecamp.org/news/python-list-remove-how-to-remove-an-item-
        from-a-list-in-python/#:~:text=The%20remove()%20method%20is,not%20by%20
        its%20index%20number.
"""
# Code Works

f = open("input1.txt")
f_read = f.read()

def greatest_sum(group_str):
    """
    Returns the greatest sum of a group of numbers in a string containing
    newline-separated groups of newline-separated numbers. 

    Args: 
        group_str: a string in the described format (str)

    Returns: the greatest sum of any group of numbers in the string (int)
    """
    cal_lst = []
    cal_tal = 0
    for num in group_str.split("\n"):
        if num:
            cal_tal += int(num)
        else:
            cal_lst.append(cal_tal)
            cal_tal = 0
    return max(cal_lst)

def greatest_num(group_str, n):
    """
    Returns sum of the n greatest sums of a group of numbers in a string
    containing newline-separated groups of newline-separated numbers. 

    Args: 
        group_str: a string in the described format (str)
        n: the number of greatest sums to be added (int)

    Returns: the sum of the 
        n greatest sums of any group of numbers in the string (int)
    """
    # maybe decompose into helper function for producing list
    """add to github readme information about how files are structured
    (both solns called in the Day1 file, functions written in same file
    as generic functions)"""
    cal_lst = []
    cal_tal = 0
    for num in group_str.split("\n"):
        if num:
            cal_tal += int(num)
        else:
            cal_lst.append(cal_tal)
            cal_tal = 0

    lst_maxes = []
    for n in range(n):
        lst_maxes.append(max(cal_lst))
        cal_lst.remove(max(cal_lst))

    return sum(lst_maxes)

print(greatest_sum(f_read))
print(greatest_num(f_read, 3))
f.close()