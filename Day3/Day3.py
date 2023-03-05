"""
Resources Consulted:
    https://stackoverflow.com/questions/63915659/create-dictionary-with-alphabet
        -characters-mapping-to-numbers
"""
f = open("input3.txt")
f_read = f.read()

def sum_priority(l_string):
    # generating alphabet dictionary
    alpha_dict = {}
    alpha_str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for idx, let in enumerate(alpha_str):
        alpha_dict[let] = idx + 1

    l_lst = l_string.split("\n")
    for l_str in l_lst:
        first, second = l_str[:len(l_str)/2], l_str[len(l_str)/2:]


print(sum_priority(f_read))
f_close()