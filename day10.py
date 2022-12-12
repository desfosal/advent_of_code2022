import numpy as np

file1 = open('input_day10.txt', 'r')
lines = file1.readlines()

stripped_lines = []
for line in lines:
  stripped_line = line.strip()
  stripped_lines.append(stripped_line)

print(stripped_lines)

cycle = 0
x = 1

output = []
output.append([cycle,x])
for line in stripped_lines:

    
    instruction = line.split(" ")
    match instruction[0]:
        case "noop":
            cycle = cycle + 1
            output.append([cycle,x])
        case "addx":
            cycle +=1
            output.append([cycle,x])
            cycle +=1
            x = x + int(instruction[1])
            output.append([cycle,x])
    #output.append([cycle,x])
    #print("last done cycle: ",cycle, "Register : ",x)

#for data in output:

 #    print("After Cycle :",data[0] , "Register is: ",data[1])

number_of_cycles = len(output)

sum_of_strengths = 0

for current_cycle in range(20,230,40): 

    print("After Cycle :",output[current_cycle - 1][0] , "Register is: ",output[current_cycle - 1][1])

    signal_strength = current_cycle * output[current_cycle - 1][1]
    sum_of_strengths += signal_strength

print("Total strength : ",sum_of_strengths)


######part 2

#cycle gives position where crt is drawing
#x gives middle of sprite
#if x-1,x,x+1 overlaps crt position, draw a pixel with symbol #

screen_rows = 6
screen_columns = 40
lit_pixels = np.zeros((screen_rows,screen_columns))

for data in output:

    current_line = int(data[0]/40)
    current_column = data[0] % 40

    print("After Cycle :",data[0] , "Register is: ",data[1],"screen line is : ", current_line,"screen column is : ",current_column)

    if current_column == data[1] or current_column == data[1]-1 or current_column == data[1]+1:
        lit_pixels[current_line,current_column] = 1

# display lit pixels

for crt_line in range(0,screen_rows):
    to_display = []
    for crt_column in range(0,screen_columns):
        if lit_pixels[crt_line,crt_column] == 1:
            to_display.append("#")
        else:
            to_display.append(".")
    print("".join(to_display))

     