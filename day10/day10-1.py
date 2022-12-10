def read_input():
    program_file = open('./input.txt', 'r')
    program_file_lines = program_file.readlines()
    program_file.close()
    return program_file_lines

# 20, 60, 100, 140, 180, 220
def evaluate_cycle(x, cycle, total_signal_strength):
    if cycle == 20 or (cycle > 40 and (cycle - 20) % 40 == 0):
        total_signal_strength += x * cycle
        print('cycle: ' + str(cycle) + ' x: ' + str(x) + ' signal_strength: ' + str(cycle * x))
        print('cycle: ' + str(cycle) + ' x: ' + str(x) + ' total_signal_strength: ' + str(total_signal_strength))
        return total_signal_strength
    return total_signal_strength


def main():
    total_signal_strength = 0
    input_lines = read_input()
    x = 1
    cycle = 0
    for cmd in input_lines:
        cmd = cmd.strip()
        if cmd == 'noop':
            cycle += 1
            total_signal_strength = evaluate_cycle(x, cycle, total_signal_strength)
        elif cmd.startswith('addx'):
            cycle += 1
            total_signal_strength = evaluate_cycle(x, cycle, total_signal_strength)
            cycle += 1
            total_signal_strength = evaluate_cycle(x, cycle, total_signal_strength)
            x += int(cmd.split(' ')[1])

    print(x)
    print(cycle)
    print(total_signal_strength)


main()
