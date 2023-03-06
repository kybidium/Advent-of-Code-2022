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
    stack_lst = stack_string_list[:n1]
    command_lst = stack_string_list[n1 + 1:]
    dict_stacks = {}
    for lst in stack_lst:
        for n in range(0, len(stack_lst[0]), 3):
            if stack_lst[n:n+3] and not f"list{(n + 1)/3}" in dict_stacks:
                dict_stacks[f"list{(n + 1)/3}"] = [stack_lst[n:n+3]]
            elif stack_lst[n:n+3]:
                dict_stacks[f"list{(n + 1)/3}"].insert(0, stack_lst[n:n+3])
    for com in command_lst:
        com_split = com.split(" ")
        com_nums = [num for num in com_split[1::2]]
        print(com_nums)
    


process_stacks(f_read, 9, 9)
f.close()