section_assignment_file = open('./input.txt', 'r')
section_assignments = section_assignment_file.readlines()
section_assignment_file.close()

pairs = []
contain_counter = 0
for section_assignment_pair in section_assignments:
    section_assignment_pair = section_assignment_pair.strip()
    section1, section2 = section_assignment_pair.split(',')
    section1_number1, section1_number2 = section1.split('-')
    section1_number1 = int(section1_number1)
    section1_number2 = int(section1_number2)
    section2_number1, section2_number2 = section2.split('-')
    section2_number1 = int(section2_number1)
    section2_number2 = int(section2_number2)

    for number in range(section1_number1, section1_number2 + 1):
        if (number >= section2_number1 and number <= section2_number2):
            contain_counter += 1
            break

print(contain_counter)