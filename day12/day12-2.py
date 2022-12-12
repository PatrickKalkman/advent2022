from dijkstar import Graph, find_path

def read_input():
    map_file = open('./test-input.txt', 'r')
    map_lines = map_file.readlines()
    map_lines = [map_line.strip() for map_line in map_lines]
    map_file.close()
    return map_lines


def calculate_node_index(row_index, col_index):
    return row_index * 100 + col_index


def create_graph(map_lines):
    graph = Graph()
    rows = len(map_lines)
    cols = len(map_lines[0])
    print(str(rows) + " " + str(cols))
    for map_row_index in range(0, rows):
        for map_col_index in range(0, cols):
            if map_col_index < len(map_lines[0]) - 1:
                # left to right
                source_node_index = calculate_node_index(map_row_index, map_col_index)
                destination_node_index = calculate_node_index(map_row_index, map_col_index + 1)
                source_elevation = map_lines[map_row_index][map_col_index]
                destination_elevation = map_lines[map_row_index][map_col_index + 1]

                if source_elevation == 'S':
                    print(source_node_index)
                if source_elevation == 'E':
                    print(source_node_index)

                cost = getCostDifference(source_elevation, destination_elevation)
                graph.add_edge(source_node_index, destination_node_index, cost)

            if map_col_index > 0:
                # left to right
                source_node_index = calculate_node_index(map_row_index, map_col_index)
                destination_node_index = calculate_node_index(map_row_index, map_col_index - 1)
                source_elevation = map_lines[map_row_index][map_col_index]
                destination_elevation = map_lines[map_row_index][map_col_index - 1]
                cost = getCostDifference(source_elevation, destination_elevation)
                graph.add_edge(source_node_index, destination_node_index, cost)
            
            if map_row_index < len(map_lines) - 1:
                # top to bottom
                source_node_index = calculate_node_index(map_row_index, map_col_index)
                destination_node_index = calculate_node_index(map_row_index + 1, map_col_index)
                source_elevation = map_lines[map_row_index][map_col_index]
                destination_elevation = map_lines[map_row_index + 1][map_col_index]
                cost = getCostDifference(source_elevation, destination_elevation)
                graph.add_edge(source_node_index, destination_node_index, cost)

            if map_row_index > 0:
                # bottom to top
                source_node_index = calculate_node_index(map_row_index, map_col_index)
                destination_node_index = calculate_node_index(map_row_index - 1, map_col_index)
                source_elevation = map_lines[map_row_index][map_col_index]
                destination_elevation = map_lines[map_row_index - 1][map_col_index]
                cost = getCostDifference(source_elevation, destination_elevation)
                graph.add_edge(source_node_index, destination_node_index, cost)

    return graph


def getCostDifference(source_elevation, destination_elevation):
    destination_cost = getCost(destination_elevation)
    elevation_delta = destination_cost - getCost(source_elevation)
    if elevation_delta > 1:
        return elevation_delta * 100
    else:
        return elevation_delta


def getCost(elevation):
    if elevation == 'S':
        elevation = 'a'
    elif elevation == 'E':
        elevation = 'z'
    return ord(elevation) - 96


def main():
    map_lines = read_input()
    graph = create_graph(map_lines)

    steps = []
    rows = len(map_lines)
    cols = len(map_lines[0])
    for map_row_index in range(0, rows):
        for map_col_index in range(0, cols):
            if map_lines[map_row_index][map_col_index] == 'a':
                source_node_index = calculate_node_index(map_row_index, map_col_index)
                shortest_path = find_path(graph, source_node_index, 205)
                #print("steps: " + str(len(shortest_path.nodes) - 1))
                steps.append(len(shortest_path.nodes) - 1)

    steps.sort()
    print(steps)


if __name__ == "__main__":
    main()

# Sabqponm
# abcryxxl
# accszExk
# acctuvwj
# abdefghi

# S => elevation a
# E => elevation z