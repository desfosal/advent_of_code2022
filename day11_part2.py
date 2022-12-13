from advent_tools import *

import numpy as np

stripped_lines = read_lines("input_day11_small.txt")

class Monkey:

    def __init__(self,number,items,operation,divisor,success_target,fail_target):

        self.items = items 
        self.number = number
        self.operation = operation
        self.divisor = divisor
        self.success_target = int(success_target)
        self.fail_target = int(fail_target)

        self.worry_level = 0

        self.inspections = 0

    def clear_items(self):
        self.items = []

    def add_item(self,item):
        self.items.append(item)

    def take_turn(self):

        targets = []
        thrown_items = []

        for item in self.items:

            self.worry_level = int(item)

            self.inspections += 1

            match self.operation[1]:

                case "+":
                    if self.operation[2] == "old":
                        self.worry_level = self.worry_level + self.worry_level
                    else:
                        self.worry_level = self.worry_level + int(self.operation[2])
                
                case "*":
                    if self.operation[2] == "old":
                        self.worry_level = self.worry_level * self.worry_level
                    else:
                        self.worry_level = self.worry_level * int(self.operation[2])

            ##self.worry_level = int(np.floor( self.worry_level / 3 )) #not needed for part 2
            print("Worry level is : ",self.worry_level)
            thrown_items.append(self.worry_level)

            if self.worry_level % int(self.divisor) == 0:
                targets.append(self.success_target)
            else:
                targets.append(self.fail_target)

        return thrown_items,targets   
           


#number_of_monkeys = 4

lines_per_monkey = 7

monkeys = []

current_monkey_number = 0

for current_line in range(0,len(stripped_lines),lines_per_monkey):

    print(stripped_lines[current_line])

    item_line = stripped_lines[current_line + 1].split(":")
    items = item_line[1].replace(" ", "").split(",")

    operation_line = stripped_lines[current_line + 2].split(":")
    operation_line_contents = operation_line[1].split(" ")
    operation = operation_line_contents[3:]

    test_line = stripped_lines[current_line + 3].split(" ")
    divisor = test_line[-1]

    success_line = stripped_lines[current_line + 4].split(" ")
    success_target = success_line[-1]

    fail_line = stripped_lines[current_line + 5].split(" ")
    fail_target = fail_line[-1]

    
    

    monkey = Monkey(current_monkey_number,items,operation,divisor,success_target,fail_target)
    current_monkey_number +=1
    monkeys.append(monkey)

    print("test")

print("number of monkeys : ",len(monkeys))

for round in range(1000):

    for monkey in monkeys:
        thrown_items,targets = monkey.take_turn()
        monkey.clear_items()

        for item_index in range(len(thrown_items)):
            monkeys[targets[item_index]].add_item(thrown_items[item_index]) ##rendu ici faut coder add_item

for monkey in monkeys:
    print("Monkey number : ",monkey.number, " Monkey items : ",monkey.items)

inspections = []
for monkey in monkeys:
    print("Monkey number : ",monkey.number, " Monkey inspections : ",monkey.inspections)
    inspections.append(monkey.inspections)

inspections.sort()
print(inspections)
max1=inspections[-1]
max2=inspections[-2]

print("Monkey business : ",max1*max2)