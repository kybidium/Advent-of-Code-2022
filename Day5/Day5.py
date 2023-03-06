# need to generalize for n stacks of height n
f = open("input5.txt")
f_read = f.read()

def process_stacks(stack_string):
    stack_string_list = stack_string.split("\n")
    stack_str = stack_string_list[:9]
    command_str = stack_string_list[10:]
    print(str(stack_str)+ "nyuguh", str(command_str))

process_stacks(f_read)
f.close()