"""
Resources Consulted:
    https://stackoverflow.com/questions/63915659/create-dictionary-with-alphabet
        -characters-mapping-to-numbers
"""
#Code Works

f = open("input3.txt")
f_read = f.read()

def alpha_gen():
    """
    """
    # generating alphabet-to-value dictionary
    alpha_dict = {}
    alpha_str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for idx, let in enumerate(alpha_str):
        alpha_dict[let] = idx + 1
    return alpha_dict

def sum_priority(l_string):
    """
    """
    # create alphabet-to-value dictionary
    alpha_dict = alpha_gen()

    prio_tot = 0
    l_lst = l_string.split("\n")
    for l_str in l_lst:
        first, second = l_str[:(len(l_str)//2)], l_str[(len(l_str)//2):]
        for s_let in first:
            if s_let in second:
                prio_tot += alpha_dict[s_let]
                break
    
    return prio_tot       

def sum_type_priority(l_string, n2):
    """
    
    """
    # create alphabet-to-value dictionary
    alpha_dict = alpha_gen()

    prio_tot = 0
    l_lst = l_string.split("\n")
    for n in range(0, len(l_lst), n2):
        lst_smol = l_lst[n:n+n2]
        for let in list(alpha_dict):
            tally = 0
            for s_let in lst_smol:
                if let in s_let:
                    tally += 1
            if tally == n2:
                prio_tot += alpha_dict[let]
                broken = True
                tally = 0
                break

    return prio_tot    

# generalize for groups of n elvess
# have alpha string generation function
# figure out less degenerate way (avoiding 3 for loops somehow)
print(sum_priority(f_read))
print(sum_type_priority(f_read, 3))
f.close()
