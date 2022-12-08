trees_file = open('./input.txt', 'r')
tree_lines = trees_file.readlines()
trees_file.close()

tree_map = []
index = 0
for tree_line in tree_lines:
    tree_map.append([])
    for tree in tree_line.strip():
        tree_map[index].append(int(tree))
    index += 1

visible_tree_count = 0
highest_scenic_score = 0
for row_index in range(0, len(tree_map)):
    for col_index in range(0, len(tree_map[row_index])):

        # Calculate scenic score left
        row_check_index = row_index
        col_check_index = col_index - 1
        scenic_score_left = 0
        while col_check_index >= 0:
            scenic_score_left += 1
            if tree_map[row_check_index][col_check_index] >= tree_map[row_index][col_index]:
                break
            col_check_index -= 1

        # Calculate scenic score right
        row_check_index = row_index
        col_check_index = col_index + 1
        scenic_score_right = 0
        while col_check_index < len(tree_map[row_index]):
            scenic_score_right += 1
            if tree_map[row_check_index][col_check_index] >= tree_map[row_index][col_index]:
                break
            col_check_index += 1

        # Calculate scenic score up
        row_check_index = row_index - 1
        col_check_index = col_index
        scenic_score_up = 0
        while row_check_index >= 0:
            scenic_score_up += 1
            if tree_map[row_check_index][col_check_index] >= tree_map[row_index][col_index]:
                break
            row_check_index -= 1

        # Calculate scenic score down
        row_check_index = row_index + 1
        col_check_index = col_index
        scenic_score_down = 0
        while row_check_index < len(tree_map[row_index]):
            scenic_score_down += 1
            if tree_map[row_check_index][col_check_index] >= tree_map[row_index][col_index]:
                break
            row_check_index += 1

        scenic_score = scenic_score_left * scenic_score_right * scenic_score_up * scenic_score_down

        print("Scenic score for row %d, col %d: %d" % (row_index, col_index, scenic_score))
        if scenic_score > highest_scenic_score:
            highest_scenic_score = scenic_score

print(highest_scenic_score)