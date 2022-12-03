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

def get_priority(toy):

    ascii = ord(toy)

    if ascii >=65 and ascii <= 90:
        return ascii -65 + 27
    elif ascii >= 97 and ascii <= 122:
        return ascii - 96

    return "PROBLEMMMMMMMMM"

for line in lines:

    stripped_line = line.strip()
    #print(stripped_line)
    number_of_items = len(stripped_line)
    #print("number of items :",number_of_items)
    compartment1 = stripped_line[0:int(number_of_items/2)]
    compartment2 = stripped_line[int(number_of_items/2):]

    #print("first compartment :" ,compartment1)
    #print("second compartment :",compartment2)

    duplicate_item = find_duplicate(compartment1,compartment2)

    priority = get_priority(duplicate_item)
    #print("duplicate : ",duplicate_item,"priority",priority)

    sum_of_priorities = sum_of_priorities + priority

print(sum_of_priorities)
    