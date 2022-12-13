def read_input():
    packets_file = open('./test-input.txt', 'r')
    packet_lines = packets_file.readlines()
    packet_lines = [packet_line.strip() for packet_line in packet_lines]
    packets_file.close()
    return packet_lines

def get_pairs(packet_lines):
    packet_pairs = []
    for packet_index in range(0, len(packet_lines), 3):
        packet_pairs.append((packet_lines[packet_index], packet_lines[packet_index + 1]))
    return packet_pairs

def compair(packet_pair):
    # [1,1,3,1,1]
    # [1,1,5,1,1]

    # [[1],[2,3,4]]
    # [[1],4]

    right_packet_index = 0
    left_packet_index = 0
    is_correct_order = True
    comparing = True
    while comparing:

        if left_packet_index >= len(packet_pair[0]) or right_packet_index >= len(packet_pair[1]):
            comparing = False
            if left_packet_index == right_packet_index:
                is_correct_order = True
            
            if left_packet_index == len(packet_pair[0]) and right_packet_index < len(packet_pair[1]):
                is_correct_order = True
            
            if right_packet_index == len(packet_pair[1]) and left_packet_index < len(packet_pair[0]):
                is_correct_order = True

            continue

        left_char = packet_pair[0][left_packet_index]
        right_char = packet_pair[1][right_packet_index]
        if ((left_char == '[' and right_char == '[') or
            (left_char == ']' and right_char == ']') or
            (left_char == ',' and right_char == ']') or
            (left_char == ']' and right_char == ',') or
            (left_char == ',' and right_char == ',')):
            left_packet_index += 1
            right_packet_index += 1
            continue

        if left_char == '[' and right_char.isnumeric():
            left_packet_index += 1
            continue

        if right_char == '[' and left_char.isnumeric():
            right_packet_index += 1
            continue


        if left_char.isnumeric() and right_char.isnumeric():
            print("Comparing " + left_char + " and " + right_char + " as numbers")
            if int(left_char) > int(right_char):
                is_correct_order = False
                comparing = False

        left_packet_index += 1
        right_packet_index += 1
    
    return is_correct_order


def main():
    index_sum = 0
    packet_lines = read_input()
    packet_pairs = get_pairs(packet_lines)
    for pair_index in range(0, len(packet_pairs)):
        print("Comparing " + str(packet_pairs[pair_index]))
        is_correct_order = compair(packet_pairs[pair_index])
        if is_correct_order:
            index_sum += (pair_index + 1)
            print("Pair " + str(packet_pairs[pair_index]) + " is in the correct order.")
        else:
            print("Pair " + str(packet_pairs[pair_index]) + " is not in the correct order.")

    print("The sum of the index of the correct pairs is " + str(index_sum))
        




if __name__ == "__main__":
    main()