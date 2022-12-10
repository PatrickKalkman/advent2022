def read_input():
    program_file = open('./input.txt', 'r')
    program_file_lines = program_file.readlines()
    program_file.close()
    return program_file_lines


line_chars = [''] * 40
index = 0


# 20, 60, 100, 140, 180, 220
def evaluate_cycle(x):
    global index
    if index == x or index == x - 1 or index == x + 1:
        line_chars[index] = '#'
    else:
        line_chars[index] = '.'

    # print('cycle: ' + str(cycle) + ' x: ' + str(x) + ' index: ' + str(index) + ' char: ' + line_chars[index])

    if index == 39:
        index = 0
        line = ""
        for char in line_chars:
            line += char
        print(line)
    else:
        index += 1


def main():
    input_lines = read_input()
    x = 1
    cycle = 0
    for cmd in input_lines:
        cmd = cmd.strip()
        if cmd == 'noop':
            cycle += 1
            evaluate_cycle(x)
        elif cmd.startswith('addx'):
            cycle += 1
            evaluate_cycle(x)
            cycle += 1
            evaluate_cycle(x)
            x += int(cmd.split(' ')[1])


main()
