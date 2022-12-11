def read_input():
    notes_file = open('./input.txt', 'r')
    notes = notes_file.readlines()
    notes_file.close()
    return notes


class Monkey:

    inspected = 0

    def __init__(self, index, starting_items, division, monkey_true, monkey_false, operation_function):
        self.index = index
        self.starting_items = starting_items
        self.division = division
        self.monkey_true = monkey_true
        self.monkey_false = monkey_false
        self.operation_function = operation_function

    def operation(self, worry):
        return self.operation_function(worry)

    def getInspections(self):
        return self.inspected

    def add_item(self, item):
        self.starting_items.append(item)

    def clear(self):
        self.starting_items.clear()

    def test(self, worry):
        self.inspected += 1
        return worry % self.division == 0

    def bored(self, worry):
        return int(worry / 3)

    def throw_to(self, worry):
        if self.test(worry):
            return self.monkey_true
        else:
            return self.monkey_false


def main():
    # notes = read_input()

    m0 = Monkey(0, [89, 95, 92, 64, 87, 68], 2, 7, 4, lambda x: x * 11)
    m1 = Monkey(1, [87, 67], 13, 3, 6, lambda x: x + 1)
    m2 = Monkey(2, [95, 79, 92, 82, 60], 3, 1, 6, lambda x: x + 6)
    m3 = Monkey(3, [67, 97, 56], 17, 7, 0, lambda x: x * x)
    m4 = Monkey(4, [80, 68, 87, 94, 61, 59, 50, 68], 19, 5, 2, lambda x: x * 7)
    m5 = Monkey(5, [73, 51, 76, 59], 7, 2, 1, lambda x: x + 8)
    m6 = Monkey(6, [92], 11, 3, 0, lambda x: x + 5)
    m7 = Monkey(7, [99, 76, 78, 76, 79, 90, 89], 5, 4, 5, lambda x: x + 7)

    monkeys = [m0, m1, m2, m3, m4, m5, m6, m7]

    for round in range(1, 21):
        for monkey in monkeys:
            for item in monkey.starting_items:
                worry = monkey.operation(item)
                worry = monkey.bored(worry)
                monkey_index = monkey.throw_to(worry)
                monkeys[monkey_index].add_item(worry)
            monkey.clear()

    monkeys.sort(key=lambda x: x.getInspections(), reverse=True)
    for monkey in monkeys:
        print("Monkey %d: %d" % (monkey.index, monkey.getInspections()))

    print("Total monkey business " + str(monkeys[0].getInspections() * monkeys[1].getInspections()))


if __name__ == "__main__":
    main()

# Monkey 0:
#   Starting items: 89, 95, 92, 64, 87, 68
#   Operation: new = old * 11
#   Test: divisible by 2
#     If true: throw to monkey 7
#     If false: throw to monkey 4

# Monkey 1:
#   Starting items: 87, 67
#   Operation: new = old + 1
#   Test: divisible by 13
#     If true: throw to monkey 3
#     If false: throw to monkey 6

# Monkey 2:
#   Starting items: 95, 79, 92, 82, 60
#   Operation: new = old + 6
#   Test: divisible by 3
#     If true: throw to monkey 1
#     If false: throw to monkey 6

# Monkey 3:
#   Starting items: 67, 97, 56
#   Operation: new = old * old
#   Test: divisible by 17
#     If true: throw to monkey 7
#     If false: throw to monkey 0

# Monkey 4:
#   Starting items: 80, 68, 87, 94, 61, 59, 50, 68
#   Operation: new = old * 7
#   Test: divisible by 19
#     If true: throw to monkey 5
#     If false: throw to monkey 2

# Monkey 5:
#   Starting items: 73, 51, 76, 59
#   Operation: new = old + 8
#   Test: divisible by 7
#     If true: throw to monkey 2
#     If false: throw to monkey 1

# Monkey 6:
#   Starting items: 92
#   Operation: new = old + 5
#   Test: divisible by 11
#     If true: throw to monkey 3
#     If false: throw to monkey 0

# Monkey 7:
#   Starting items: 99, 76, 78, 76, 79, 90, 89
#   Operation: new = old + 7
#   Test: divisible by 5
#     If true: throw to monkey 4
#     If false: throw to monkey 5