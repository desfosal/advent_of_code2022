file1 = open('input_day_1.txt', 'r')
lines = file1.readlines()


file1 = open('input_day_1.txt', 'r')
lines = file1.readlines()

best_elf = -1
best_elf_calories = -1
most_calories = -1

current_elf = 1 


for current_line in lines[0:12]:
   # calories = int(current_line)
    #print(test)
    if current_line=="\n":
        print("got it")
        print(len(current_line))
        
    else:
        print("empty!")