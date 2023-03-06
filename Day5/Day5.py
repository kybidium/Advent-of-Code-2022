"""
Resources Consulted:
    https://www.tutorialspoint.com/what-is-a-negative-indexing-in-python#:~:text
        =Negative%20Indexing%20is%20used%20to,i.e.%20start%2C%20stop%20and%20step.
"""
# need to generalize for automatically using n2 stacks of height n1 (unknown ns)
f = open("input5.txt")
f_read = f.read()

def process_stacks(stack_string, n1, n2):
    """
    Args:
        n1: index of line after stack part of string
        n2: number of stacks
    """
    stack_string_list = stack_string.strip().split("\n")
    stack_lst = stack_string_list[:n1 - 1]
    command_lst = stack_string_list[n1:]
    dict_stacks = {}
    for lst in stack_lst:
        for n in range(0, len(stack_lst[0]), 3):
            if lst[n:n+3] and not f"list{(n)//3}" in dict_stacks:
                dict_stacks[f"list{(n)//3}"] = [lst[n:n+3]]
            elif lst[n:n+3]:
                dict_stacks[f"list{(n)//3}"].insert(0, str(lst[n:n+3]))
    print(dict_stacks)
    tru_com_lst = []
    for com in command_lst:
        com_split = com.split(" ")
        com_nums = [num for num in com_split[1::2]]
        tru_com_lst.append(com_nums)
    
    for coms in tru_com_lst:
        stack1 = dict_stacks[f"list{coms[1]}"]
        stack2 = dict_stacks[f"list{coms[2]}"]

        stack2.extend(stack1[len(stack1) - coms[0] - 1:])
        del stack1[len(stack1) - coms[0] - 1:]

    str_stacks_fin = ""
    for stack in dict_stacks.get_values():
        str_stacks_fin += stack[-1]

    return str_stacks_fin

process_stacks(f_read, 9, 9)
f.close()