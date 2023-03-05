f = open("input.txt")
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

print(greatest_sum(f_read))
        

        
