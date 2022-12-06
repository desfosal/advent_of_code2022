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

print(stacks)