
def read_input():
    head_moves_file = open('./input.txt', 'r')
    head_moves = head_moves_file.readlines()
    head_moves_file.close()
    return head_moves


def move_tail(hp, tp):

    y_distance_abs = abs(hp[0] - tp[0])
    x_distance_abs = abs(hp[1] - tp[1])

    y_distance_positive = hp[0] - tp[0] > 0
    x_distance_positive = hp[1] - tp[1] > 0

    if y_distance_abs > 1 and x_distance_abs == 0:
        if y_distance_positive:
            tp = (tp[0] + 1, tp[1])
        else:
            tp = (tp[0] - 1, tp[1])

    if x_distance_abs > 1 and y_distance_abs == 0:
        if x_distance_positive:
            tp = (tp[0], tp[1] + 1)
        else:
            tp = (tp[0], tp[1] - 1)

    if y_distance_abs > 1 and x_distance_abs == 1:
        if y_distance_positive and x_distance_positive:
            tp = (tp[0] + 1, tp[1] + 1)
        elif y_distance_positive and not x_distance_positive:
            tp = (tp[0] + 1, tp[1] - 1)
        elif not y_distance_positive and x_distance_positive:
            tp = (tp[0] - 1, tp[1] + 1)
        elif not y_distance_positive and not x_distance_positive:
            tp = (tp[0] - 1, tp[1] - 1)

    if x_distance_abs > 1 and y_distance_abs == 1:
        if y_distance_positive and x_distance_positive:
            tp = (tp[0] + 1, tp[1] + 1)
        elif y_distance_positive and not x_distance_positive:
            tp = (tp[0] + 1, tp[1] - 1)
        elif not y_distance_positive and x_distance_positive:
            tp = (tp[0] - 1, tp[1] + 1)
        elif not y_distance_positive and not x_distance_positive:
            tp = (tp[0] - 1, tp[1] - 1)

    if x_distance_abs > 1 and y_distance_abs > 1:
        if y_distance_positive and x_distance_positive:
            tp = (tp[0] + 1, tp[1] + 1)
        elif y_distance_positive and not x_distance_positive:
            tp = (tp[0] + 1, tp[1] - 1)
        elif not y_distance_positive and x_distance_positive:
            tp = (tp[0] - 1, tp[1] + 1)
        elif not y_distance_positive and not x_distance_positive:
            tp = (tp[0] - 1, tp[1] - 1) 

    return tp


def create_matrix(x, y):
    matrix = []
    for i in range(0, y):
        matrix.append([])
        for j in range(0, x):
            matrix[i].append('.')
    return matrix


def reset_matrix(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            matrix[i][j] = '.'


def print_matrix(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            print(matrix[i][j], end='')
        print()

def print_matrix_focus(matrix, focus_point):
    for i in range(focus_point[0] - 4, focus_point[0] + 4):
        for j in range(focus_point[1] - 4, focus_point[1] + 4):
            print(matrix[i][j], end='')
        print()


def count_visited(matrix):
    visited = 0
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if matrix[i][j] == '#':
                visited += 1
    return visited


def make_moves(start_position, matrix, head_moves, record_matrix, number_of_tails):
    current_head_position = start_position
    tails_position = []
    for i in range(0, number_of_tails):
        tails_position.append(start_position)

    yx_move = (0, 0)
    move_index = 1
    for move in head_moves:
        print(move.strip())
        move_index += 1
        direction = move.split(' ')[0]
        places = int(move.split(' ')[1])
        if direction == 'R':
            yx_move = (0, 1)
        if direction == 'L':
            yx_move = (0, -1)
        if direction == 'U':
            yx_move = (-1, 0)
        if direction == 'D':
            yx_move = (1, 0)

        for i in range(0, places):
            #reset_matrix(matrix)
            current_head_position = (current_head_position[0] + yx_move[0], current_head_position[1] + yx_move[1])

            head = current_head_position
            for tail_index in range(0, len(tails_position)):
                tails_position[tail_index] = move_tail(head, tails_position[tail_index])
                head = tails_position[tail_index]

            for tail_index in range(len(tails_position) - 1, -1, -1):
                matrix[tails_position[tail_index][0]][tails_position[tail_index][1]] = str(tail_index + 1)
            matrix[current_head_position[0]][current_head_position[1]] = 'H'

            record_matrix[tails_position[8][0]][tails_position[8][1]] = '#'
            # print_matrix_focus(matrix,current_head_position)
            #print_matrix(matrix)
            #print("")

    return current_head_position


matrix_size = (500, 500)
#matrix_size = (6, 5)
#matrix_size = (27, 22)
head_moves = read_input()
matrix = create_matrix(matrix_size[0], matrix_size[1])
record_matrix = create_matrix(matrix_size[0], matrix_size[1])
start_position = (106, 89)
#start_position = (16, 11)

current_head_position = make_moves(start_position, matrix, head_moves, record_matrix, 9)
#print(current_head_position)
#print_matrix(record_matrix)
print(count_visited(record_matrix))
