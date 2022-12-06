file1 = open('input_day5.txt', 'r')
lines = file1.readlines()

##parsing crates
number_of_stacks = 9

stacks = [] #list of lists, each sublist is a stack of crates
for i in range(number_of_stacks):
    stacks.append([])

#starting with the bottom of the pile, fill each stack 
for line in lines[7::-1]:
    #print(line)
    #print(line[1::4])
    crates = line[1::4]     

    for index in range(number_of_stacks):

        if not (crates[index] == " "):
            stacks[index].append(crates[index])

for line in lines[10:]:
    print(line)
    splitted_line = line.split(" ")

    how_many = int(splitted_line[1])
    origin = int(splitted_line[3]) - 1 # python index starts at 0, stack number starts at 1
    destination = int(splitted_line[5]) - 1
    print(how_many,origin,destination)

    #origin_stack = stacks[origin]
    #destination_stack = stacks[destination]

    for counter in range(how_many):

        crate = stacks[origin].pop()
        stacks[destination].append(crate)

print(stacks)

for stack in stacks:
    print(stack[-1])