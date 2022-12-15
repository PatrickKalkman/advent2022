def read_input():
    sensors_file = open('./input.txt', 'r')
    sensors = sensors_file.readlines()
    sensors = [sensor.strip() for sensor in sensors]
    sensors_file.close()
    return sensors


def parse_sensors(sensors_beacons):
    sensors_and_beacons = []
    for sensor_beacon_line in sensors_beacons:
        sensor_beacon = sensor_beacon_line.split(': closest beacon is at ')
        sensor = sensor_beacon[0].replace('Sensor at ', '')
        coords = sensor.split(', ')
        sx = int(coords[0].replace('x=', ''))
        sy = int(coords[1].replace('y=', ''))
        beacon = sensor_beacon[1].split(', ')
        bx = int(beacon[0].replace('x=', ''))
        by = int(beacon[1].replace('y=', ''))
        dx = abs(bx - sx)
        dy = abs(by - sy)
        manhattan = dx + dy
        sensors_and_beacons.append(((sx, sy), (bx, by), manhattan))

    return sensors_and_beacons


def get_matrix_size(sensors_beacons):
    max_x = 0
    max_y = 0
    min_x = 100000000
    min_y = 100000000
    for sensor, beacon, _ in sensors_beacons:
        if sensor[0] > max_x:
            max_x = sensor[0]
        if sensor[1] > max_y:
            max_y = sensor[1]
        if beacon[0] > max_x:
            max_x = beacon[0]
        if beacon[1] > max_y:
            max_y = beacon[1]
        if sensor[0] < min_x:
            min_x = sensor[0]
        if sensor[1] < min_y:
            min_y = sensor[1]
        if beacon[0] < min_x:
            min_x = beacon[0]
        if beacon[1] < min_y:
            min_y = beacon[1]

    real_max_x = 0 - min_x + max_x
    real_max_y = 0 - min_y + max_y

    return real_max_x, real_max_y, abs(min_x)


def fill_matrix_with_sensors_and_beacons(matrix, sensors_beacons, x_shift, y_shift):
    for sensor, beacon, _ in sensors_beacons:
        matrix[sensor[1]+ y_shift][sensor[0] + x_shift] = 'S'
        matrix[beacon[1]+ y_shift][beacon[0] + x_shift] = 'B'

    return matrix


def create_empty_matrix(matrix_size):
    matrix = []
    for y in range(matrix_size[1] + 1):
        matrix.append([])
        for _ in range(matrix_size[0] + 1):
            matrix[y].append('.')

    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(''.join(row))


def draw_sensor_range(sensors_and_beacons, matrix, x_shift, y_shift):
    sensor_index = 1
    for sensor, beacon, manhattan in sensors_and_beacons:
        print(sensor_index)
        sensor_index += 1
        for y in range(sensor[1] - manhattan, sensor[1] + manhattan + 1):
            distance = abs(y - sensor[1])
            for x in range(sensor[0] + 2 - manhattan + distance, sensor[0] + x_shift + 1):
                if x >= 0 and y >= 0 and x < len(matrix[0]) and y < len(matrix):
                    if matrix[y][x] == '.':
                        matrix[y][x] = '#'

            for x in range(sensor[0] + x_shift, sensor[0] + x_shift + 1 + manhattan - distance):
                if x >= 0 and y >= 0 and x < len(matrix[0]) and y < len(matrix):
                    if matrix[y][x] == '.':
                        matrix[y][x] = '#'


def count_row(row, matrix):
    not_available = 0
    for x in range(len(matrix[row])):
        if matrix[row][x] == '#':
            not_available += 1

    return not_available


def main():
    sensors = read_input()
    sensors_beacons = parse_sensors(sensors)
    print(sensors_beacons)
    matrix_size = get_matrix_size(sensors_beacons)
    print(matrix_size)
    matrix = create_empty_matrix(matrix_size)
    matrix_with_sensors_and_beacons = fill_matrix_with_sensors_and_beacons(matrix, sensors_beacons, matrix_size[2], 0)
    draw_sensor_range(sensors_beacons, matrix_with_sensors_and_beacons, matrix_size[2], 0)
    print_matrix(matrix_with_sensors_and_beacons)
    not_available = count_row(2000000, matrix_with_sensors_and_beacons)
    print(not_available)

if __name__ == "__main__":
    main()
