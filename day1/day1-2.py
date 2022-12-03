
calories = open('calories.txt', 'r')
calorie_lines = calories.readlines()
calories.close()

elf = 1
calories = 0
elves = []

for line in calorie_lines:
    if line.strip() == "":
        elves.append(calories)
        print('Elf ' + str(elf) + ' ate ' + str(calories) + ' calories')
        elf += 1
        calories = 0
    else:
        calories += int(line.strip())

elves.sort()

print('Top 3 elves ate ' + str(elves[-1] + elves[-2] + elves[-3]) +
      ' calories')
