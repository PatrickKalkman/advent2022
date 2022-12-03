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
for rucksack in rucksack_contents:
    rucksack = rucksack.strip()
    first_compartment, second_compartment = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
    for first_compartment_char in first_compartment:
        if first_compartment_char in second_compartment:
            found = True
            score += priorities[first_compartment_char]
            break

    if not found:
        for second_compartment_char in second_compartment:
            if second_compartment_char in first_compartment:
                score += priorities[second_compartment_char]
                break

print(score)
