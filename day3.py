file1 = open('input_day3.txt', 'r')
lines = file1.readlines()

sum_of_priorities = 0

def find_duplicate(compartment1,compartment2):

    for i in range( len( compartment1 ) ):

        compartment1_toy = compartment1[i]

        for j in range( len( compartment2 ) ):

            compartment2_toy = compartment2[j]

            if compartment1_toy == compartment2_toy:
                return compartment1_toy

    return 'PROBLEMMMMMM'

def find_badge(elf1,elf2,elf3):

    badge = (set(elf1).intersection(elf2)).intersection(elf3)

    return list(badge)[0]

def get_priority(toy):

    ascii = ord(toy)

    if ascii >=65 and ascii <= 90:
        return ascii -65 + 27
    elif ascii >= 97 and ascii <= 122:
        return ascii - 96

    return "PROBLEMMMMMMMMM"


################part 1#################
for line in lines:

    stripped_line = line.strip()
    
    number_of_items = len(stripped_line)
    
    compartment1 = stripped_line[0:int(number_of_items/2)]
    compartment2 = stripped_line[int(number_of_items/2):]    

    duplicate_item = find_duplicate(compartment1,compartment2)

    priority = get_priority(str(duplicate_item))    

    sum_of_priorities = sum_of_priorities + priority

print("Priorities part 1 : ",sum_of_priorities)

############### part 2
sum_of_priorities = 0

for index in range(0,len(lines)-2,3):

    line1 = lines[index].strip()
    line2 = lines[index+1].strip()
    line3 = lines[index+2].strip()    
    
    badge = find_badge(line1,line2,line3)     

    priority = get_priority(str(badge))    

    sum_of_priorities = sum_of_priorities + priority

print("priorities part 2 : ",sum_of_priorities)




    