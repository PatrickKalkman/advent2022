from treelib import Node, Tree

tree = Tree()


def build_tree(shell_lines):
    current_node = None
    root_node = None
    node_index = 0
    for shell_line in shell_lines:
        node_index += 1
        shell_line = shell_line.strip()
        if shell_line.startswith('$ cd /'):
            current_node = tree.create_node("root", "root", data={})
            root_node = current_node
            print("adding root")
        elif shell_line[0].isdigit():
            line_parts = shell_line.split(' ')
            current_node.data[line_parts[1]] = int(line_parts[0])
            print("adding file " + line_parts[1] + " " + line_parts[0])
        elif shell_line.startswith('$ cd ..'):
            current_node = tree.parent(current_node.identifier)
            print("going up: " + current_node.identifier)
        elif shell_line.startswith('$ cd '):
            line_parts = shell_line.split('$ cd ')
            print("adding node: " + line_parts[1])
            current_node = tree.create_node(line_parts[1], line_parts[1] + " " + str(node_index), parent=current_node.identifier, data={})

    tree.show()
    return root_node


def calculate_nodes(node):
    total = 0
    for child_node in tree.children(node.identifier):
        total = calculate_nodes(child_node)

    for key in node.data:
        total += node.data[key]

    node.data['total'] = total

    return total


shell_output_file = open('./input.txt', 'r')
shell_lines = shell_output_file.readlines()
shell_output_file.close()

root_node = build_tree(shell_lines)
total = calculate_nodes(root_node)

sub_total = 0
for node in tree.all_nodes_itr():
    if (node.data['total'] <= 100000):
        sub_total += node.data['total']
        # print(node.identifier, node.data)

print("answer = " + str(sub_total))
