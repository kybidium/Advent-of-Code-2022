# need to generalize for n stacks of height n
f = open("input5.txt")
f_read = f.read()

def process_stacks(stack_string):
    stack_str = stack_string[:9]
    command_str = stack_string[10:]
    print(stack_str, command_str)
f.close()