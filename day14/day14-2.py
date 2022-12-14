import time


def read_input():
    lines_file = open('./input.txt', 'r')
    lines = lines_file.readlines()
    lines = [line.strip() for line in lines]
    lines_file.close()
    return lines


def create_line_tuples(lines):
    tuples = []
    for line in lines:
        coords = line.split(' -> ')
        for coord_index in range(len(coords) - 1):
            first_coord = coords[coord_index]
            second_coord = coords[coord_index + 1]
            first_coord = first_coord.split(',')
            first_coord = (int(first_coord[0]), int(first_coord[1]))
            second_coord = second_coord.split(',')
            second_coord = (int(second_coord[0]), int(second_coord[1]))
            tuples.append((first_coord, second_coord))

    return tuples


def determine_matrix_size(tuples):
    max_x = 0
    max_y = 0
    min_x = 1000
    min_y = 0
    for coord_pair in tuples:
        for coord in coord_pair:
            if coord[0] > max_x:
                max_x = coord[0]
            if coord[1] > max_y:
                max_y = coord[1]
            if coord[0] < min_x:
                min_x = coord[0]
            if coord[1] < min_y:
                min_y = coord[1]
    return (min_x, min_y, max_x, max_y)


def print_matrix(matrix):
    for row in matrix:
        print(''.join(row)) 


def draw_lines(matrix, tuples, matrix_size):
    for coord_pair in tuples:
        first_coord = coord_pair[0]
        second_coord = coord_pair[1]
        # ßprint(first_coord, second_coord)
        if first_coord[0] == second_coord[0]:
            # vertical line
            y_start = first_coord[1] - matrix_size[1]
            y_end = second_coord[1] - matrix_size[1]
            # print("vertical from " + str(y_start) + " to " + str(y_end))
            x = first_coord[0] - matrix_size[0]
            for y in range(y_start, y_end + 1):
                matrix[y][x] = '#'
        elif first_coord[1] == second_coord[1]:
            x_start = first_coord[0] - matrix_size[0]
            x_end = second_coord[0] - matrix_size[0]
            if x_start > x_end:
                x_start, x_end = x_end, x_start
            # print("horizontal from " + str(x_start) + " to " + str(x_end))
            y = first_coord[1] - matrix_size[1]
            for x in range(x_start, x_end + 1):
                matrix[y][x] = '#'


def simulate_sand(matrix, matrix_size):
    frame_counter = 0
    sand_start = (500 - matrix_size[0], 0)
    sand_location = sand_start
    previous_location = sand_start
    sand_counter = 0
    while True:
        frame_counter += 1
        matrix[previous_location[1]][previous_location[0]] = '.'
        matrix[sand_location[1]][sand_location[0]] = 'o'
        # print("\033c", end="")
        # print_matrix(matrix)
        # time.sleep(0.1)
        previous_location = sand_location
        if ((sand_location[1] + 1) >= len(matrix) or (sand_location[0] + 1) >= len(matrix[0]) - 1):
            print(sand_location)
            print(sand_counter)
            print_matrix(matrix)
            break

        if matrix[sand_location[1] + 1][sand_location[0]] == '.':
            temp_location = list(sand_location)
            temp_location[1] += 1
            sand_location = tuple(temp_location)
        elif can_drop_left(matrix, sand_location):
            temp_location = list(sand_location)
            temp_location[1] += 1
            temp_location[0] -= 1
            sand_location = tuple(temp_location)
        elif can_drop_right(matrix, sand_location):
            temp_location = list(sand_location)
            temp_location[1] += 1
            temp_location[0] += 1
            sand_location = tuple(temp_location)
        elif is_blocked(matrix, sand_location):
            sand_location = sand_start
            previous_location = sand_start
            sand_counter += 1


def is_blocked(matrix, sand_location):
    if ((matrix[sand_location[1] + 1][sand_location[0]] == '#' or matrix[sand_location[1] + 1][sand_location[0]] == 'o') and
       (matrix[sand_location[1] + 1][sand_location[0] - 1] == '#' or matrix[sand_location[1] + 1][sand_location[0] - 1] == 'o') and
       (matrix[sand_location[1] + 1][sand_location[0] + 1] == '#' or matrix[sand_location[1] + 1][sand_location[0] + 1] == 'o')):
        return True
    return False


def can_drop_left(matrix, sand_location):
    if matrix[sand_location[1] + 1][sand_location[0] - 1] == '.':
        return True
    return False


def can_drop_right(matrix, sand_location):
    if matrix[sand_location[1] + 1][sand_location[0] + 1] == '.':
        return True
    return False


def main():
    lines = read_input()
    tuples = create_line_tuples(lines)
    # print(tuples)
    matrix_size = determine_matrix_size(tuples)
    matrix = [['.' for x in range(matrix_size[0], matrix_size[2] + 1)] for y in range(matrix_size[1], matrix_size[3] + 1)]
    draw_lines(matrix, tuples, matrix_size)
    #print_matrix(matrix)
    simulate_sand(matrix, matrix_size)


if __name__ == "__main__":
    main()