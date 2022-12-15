# Sensor at x=2, y=18: closest beacon is at x=-2, y=15
# Sensor at x=9, y=16: closest beacon is at x=10, y=16
# Sensor at x=13, y=2: closest beacon is at x=15, y=3
# Sensor at x=12, y=14: closest beacon is at x=10, y=16
# Sensor at x=10, y=20: closest beacon is at x=10, y=16
# Sensor at x=14, y=17: closest beacon is at x=10, y=16
# Sensor at x=8, y=7: closest beacon is at x=2, y=10
# Sensor at x=2, y=0: closest beacon is at x=2, y=10
# Sensor at x=0, y=11: closest beacon is at x=2, y=10
# Sensor at x=20, y=14: closest beacon is at x=25, y=17
# Sensor at x=17, y=20: closest beacon is at x=21, y=22
# Sensor at x=16, y=7: closest beacon is at x=15, y=3
# Sensor at x=14, y=3: closest beacon is at x=15, y=3
# Sensor at x=20, y=1: closest beacon is at x=15, y=3

def read_input():
    sensors_file = open('./test-input.txt', 'r')
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
    min_x = 10000
    min_y = 10000
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

    return real_max_x, real_max_y


def fill_matrix_with_sensors_and_beacons(matrix, sensors_beacons):
    for sensor, beacon, _ in sensors_beacons:
        matrix[sensor[1]][sensor[0] + 2] = 'S'
        matrix[beacon[1]][beacon[0] + 2] = 'B'

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


def main():
    sensors = read_input()
    sensors_beacons = parse_sensors(sensors)
    matrix_size = get_matrix_size(sensors_beacons)
    matrix = create_empty_matrix(matrix_size)
    matrix_with_sensors_and_beacons = fill_matrix_with_sensors_and_beacons(matrix, sensors_beacons)
    print_matrix(matrix_with_sensors_and_beacons)


if __name__ == "__main__":
    main()