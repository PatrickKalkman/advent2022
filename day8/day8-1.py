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
for row_index in range(0, len(tree_map)):
    for col_index in range(0, len(tree_map[row_index])):
        if row_index == 0 or col_index == 0 or row_index == len(tree_map) - 1 or col_index == len(tree_map[row_index]) - 1:
            visible_tree_count += 1
            continue

        # Check left
        row_check_index = row_index
        col_check_index = col_index - 1
        left_bigger = False
        while col_check_index >= 0:
            if tree_map[row_check_index][col_check_index] >= tree_map[row_index][col_index]:
                left_bigger = True
                break
            col_check_index -= 1

        if not left_bigger:
            visible_tree_count += 1
            continue

        # Check right
        row_check_index = row_index
        col_check_index = col_index + 1
        right_bigger = False
        while col_check_index < len(tree_map[row_index]):
            if tree_map[row_check_index][col_check_index] >= tree_map[row_index][col_index]:
                right_bigger = True
                break
            col_check_index += 1

        if not right_bigger:
            visible_tree_count += 1
            continue

        # Check up
        row_check_index = row_index - 1
        col_check_index = col_index
        up_bigger = False
        while row_check_index >= 0:
            if tree_map[row_check_index][col_check_index] >= tree_map[row_index][col_index]:
                up_bigger = True
                break
            row_check_index -= 1

        if not up_bigger:
            visible_tree_count += 1
            continue

        # Check down
        row_check_index = row_index + 1
        col_check_index = col_index
        down_bigger = False
        while row_check_index < len(tree_map[row_index]):
            if tree_map[row_check_index][col_check_index] >= tree_map[row_index][col_index]:
                down_bigger = True
                break
            row_check_index += 1

        if not down_bigger:
            visible_tree_count += 1
            continue

print(visible_tree_count)