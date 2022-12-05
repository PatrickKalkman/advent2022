rucksack_file = open('./input.txt', 'r')
rucksack_contents = rucksack_file.readlines()
rucksack_file.close()

# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.

priorities = {}
priority = 1
for char in range(ord('a'), ord('z') + 1):
    priorities[chr(char)] = priority
    priority = priority + 1

for char in range(ord('A'), ord('Z') + 1):
    priorities[chr(char)] = priority
    priority = priority + 1

print(priorities)

found = False
score = 0
for rucksack_index in range(0, len(rucksack_contents), 3):
    line0 = rucksack_contents[rucksack_index].strip()
    line1 = rucksack_contents[rucksack_index + 1].strip()
    line2 = rucksack_contents[rucksack_index + 2].strip()
    for line0_char in line0:
        if line0_char in line1 and line0_char in line2:
            score += priorities[line0_char]
            break

print(score)
