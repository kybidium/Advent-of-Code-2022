"""
Resources Consulted:
    https://www.tutorialspoint.com/what-is-a-negative-indexing-in-python#:~:text
        =Negative%20Indexing%20is%20used%20to,i.e.%20start%2C%20stop%20and%20step.
"""
# Code Works
# need to generalize for automatically using n2 stacks of height n1 (unknown n's)
f = open("input5.txt")
f_read = f.read()

def process_stacks(stack_string, n1, n2):
    """
    Args:
        n1: index of line after stack part of string
        n2: number of stacks
    """
    stack_string_list = stack_string.strip().split("\n")
    # create a list of the rows of stack items
    stack_lst = stack_string_list[:n1 - 1]
    # create a list of the rows of commands
    command_lst = stack_string_list[n1 + 1:]
    dict_stacks = {}
    
    # iterating through the list of rows of stack items
    for lst in stack_lst:
        # iterating through the relevant characters in each row
        for n in range(1, len(stack_lst[0]), 4):
            # if the 
            if lst[n] == " " and not f"list{(n+3)//4}" in dict_stacks:
                dict_stacks[f"list{(n+3)//4}"] = []
            elif not lst[n] == " " and not f"list{(n+3)//4}" in dict_stacks:
                dict_stacks[f"list{(n+3)//4}"] = [lst[n]]
            elif not lst[n] == " ":
                dict_stacks[f"list{(n+3)//4}"].insert(0, lst[n])
    tru_com_lst = []
    for com in command_lst:
        com_split = com.split(" ")
        com_nums = [int(num) for num in com_split[1::2]]
        tru_com_lst.append(com_nums)
    
    for coms in tru_com_lst:
        stack1 = dict_stacks[f"list{coms[1]}"]
        stack2 = dict_stacks[f"list{coms[2]}"]
        if coms[0] != len(stack1):
            # need to fix indexing
            stack2.extend(stack1[-1:len(stack1) - coms[0] - 1:-1])
            print(coms[0],stack1, stack2, stack1[-1:len(stack1) - coms[0] - 1:-1])
            del stack1[-1:len(stack1) - coms[0] - 1:-1]
        else:
            stack2.extend(stack1[::-1])
            del stack1[::-1]

    str_stacks_fin = ""
    for n in range(0, n2):
        if dict_stacks[f"list{n+1}"]:
            str_stacks_fin += dict_stacks[f"list{n+1}"][-1]

    return str_stacks_fin

def process_stacks_mul(stack_string, n1, n2):
    """
    Args:
        n1: index of line after stack part of string
        n2: number of stacks
    """
    stack_string_list = stack_string.strip().split("\n")
    # create a list of the rows of stack items
    stack_lst = stack_string_list[:n1 - 1]
    # create a list of the rows of commands
    command_lst = stack_string_list[n1 + 1:]
    dict_stacks = {}
    
    # iterating through the list of rows of stack items
    for lst in stack_lst:
        # iterating through the relevant characters in each row
        for n in range(1, len(stack_lst[0]), 4):
            # if the 
            if lst[n] == " " and not f"list{(n+3)//4}" in dict_stacks:
                dict_stacks[f"list{(n+3)//4}"] = []
            elif not lst[n] == " " and not f"list{(n+3)//4}" in dict_stacks:
                dict_stacks[f"list{(n+3)//4}"] = [lst[n]]
            elif not lst[n] == " ":
                dict_stacks[f"list{(n+3)//4}"].insert(0, lst[n])
    tru_com_lst = []
    for com in command_lst:
        com_split = com.split(" ")
        com_nums = [int(num) for num in com_split[1::2]]
        tru_com_lst.append(com_nums)
    
    for coms in tru_com_lst:
        stack1 = dict_stacks[f"list{coms[1]}"]
        stack2 = dict_stacks[f"list{coms[2]}"]
        if coms[0] != len(stack1):
            # need to fix indexing
            stack2.extend(stack1[len(stack1) - coms[0]:])
            print(coms[0],stack1, stack2, stack1[len(stack1) - coms[0]:])
            del stack1[len(stack1) - coms[0]:]
        else:
            stack2.extend(stack1[:])
            del stack1[:]

    str_stacks_fin = ""
    for n in range(0, n2):
        if dict_stacks[f"list{n+1}"]:
            str_stacks_fin += dict_stacks[f"list{n+1}"][-1]

    return str_stacks_fin

print(process_stacks(f_read, 9, 9))
print(process_stacks_mul(f_read, 9, 9))
f.close()
"""
-3, 3
1, 1
5, 2
9, 3
13, 4
y*3 + (y - 3) = n
4y -3 = n
(n + 3)/4 = y
"""