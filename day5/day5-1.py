# [P]     [L]         [T]            
# [L]     [M] [G]     [G]     [S]    
# [M]     [Q] [W]     [H] [R] [G]    
# [N]     [F] [M]     [D] [V] [R] [N]
# [W]     [G] [Q] [P] [J] [F] [M] [C]
# [V] [H] [B] [F] [H] [M] [B] [H] [B]
# [B] [Q] [D] [T] [T] [B] [N] [L] [D]
# [H] [M] [N] [Z] [M] [C] [M] [P] [P]
#  1   2   3   4   5   6   7   8   9 

crane_movement_file = open('./input.txt', 'r')
crane_moves_initial = crane_movement_file.readlines()
crane_movement_file.close()

ship = [[] for _ in range(9)]

for line_index in range(7, -1, -1):
    stack_index = 0
    for char_index in range(1, 37, 4):
        container_letter = crane_moves_initial[line_index][char_index]
        if container_letter != ' ':
            ship[stack_index].append(container_letter)
        stack_index = stack_index + 1

crane_moves_lf = list(filter(lambda line: 'move' in line, crane_moves_initial))
crane_moves = list(map(str.strip, crane_moves_lf))

for move in crane_moves:
    parts = move.split(' from ')
    how_many = int(parts[0].replace('move ', ''))
    containers = parts[1].split(' to ')
    source_index = int(containers[0]) - 1
    destination_index = int(containers[1]) - 1
    for _ in range(how_many):
        ship[destination_index].append(ship[source_index].pop())

for index in range(9):
    print(ship[index].pop(), end='')
