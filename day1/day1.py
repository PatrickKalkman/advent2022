
calories = open('calories.txt', 'r')
calorie_lines = calories.readlines()
calories.close()

elf = 1
calories = 0
highest_calories = 0
highest_elf = 0

for line in calorie_lines:
    if line.strip() == "":
        if calories > highest_calories:
            highest_calories = calories
            highest_elf = elf
        print('Elf ' + str(elf) + ' ate ' + str(calories) + ' calories')
        elf += 1
        calories = 0
    else:
        calories += int(line.strip())

print('Elf ' + str(highest_elf) + ' ate the most ' +
      str(highest_calories) + ' calories')
