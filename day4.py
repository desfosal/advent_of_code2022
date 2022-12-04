file1 = open('input_day4.txt', 'r')
lines = file1.readlines()

def A_contains_B(assignment_A,assignment_B):

    assignment_A_start = int(assignment_A.split('-')[0])
    assignment_A_end = int(assignment_A.split('-')[1])

    assignment_B_start = int(assignment_B.split('-')[0])
    assignment_B_end = int(assignment_B.split('-')[1])

    if assignment_B_start >= assignment_A_start and assignment_B_end <= assignment_A_end:
        return True
    else:
        return False 

def overlaps(assignment_A,assignment_B): 

    return False  

number_of_contained_assignments = 0

number_of_overlaps = 0

for line in lines:

    assignments = line.strip().split(',')
    first_elf_job = assignments[0]
    second_elf_job = assignments[1]
   # print("first assignment :",first_elf_job, "second assignment : ",second_elf_job)

    if A_contains_B(first_elf_job,second_elf_job) or A_contains_B(second_elf_job,first_elf_job):
       # print("contained!")
        number_of_contained_assignments = number_of_contained_assignments + 1

print("Number of contained assignments : ",number_of_contained_assignments)