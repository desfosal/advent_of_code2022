file1 = open('input_day7.txt', 'r')
lines = file1.readlines()

stripped_lines = []
for line in lines:
  stripped_line = line.strip()
  stripped_lines.append(stripped_line)

all_directory_sizes = []

class TreeNode:     

    def __init__(self, address, parent = None):
        self.address = address
        self.parent = parent
        self.children = []
        self.size = 0
        self.children_sizes = []
        if not self.parent == None:
            self.parent.children.append(self)#rendu ici)

    def add_file_size(self,file_size):
        self.size = self.size + file_size

        if not self.parent == None:
            self.parent.add_file_size(file_size)  

    def display(self):

        all_directory_sizes.append(self.size)
        print("My adress is : ",self.address,"My size is : ",self.size) 
        for child in self.children:
            child_size = child.display()
            self.children_sizes.append(child_size)
        return self.size




root_directory = TreeNode("/")
current_directory = root_directory
print("starting")
for line in stripped_lines:

    print(line)
    line_contents = line.split(" ")

    if line_contents[0] == "$":
        if line_contents[1] == "cd":
            if line_contents[2] == "/":
                print("atroot")
                current_directory = root_directory
            elif line_contents[2] == "..":
                current_directory = current_directory.parent
            else:
                print("creating new directory")
                current_directory = TreeNode(current_directory.address +(line_contents[2])+"/",current_directory)

    print(current_directory.address)

    if (line_contents[0].isnumeric()):
       current_directory.add_file_size(int(line_contents[0]))

print("done")

#for child in root_directory.children:
 #   child.display()

root_directory.display()

test = root_directory.children_sizes

print(test)

print(all_directory_sizes)

sum_of_sizes = 0
for dir in all_directory_sizes:
    size = (int(dir))
    if size <= 100000:
        sum_of_sizes = sum_of_sizes + size

print("Sum of sizes of directories smaller than threshold : ",sum_of_sizes)


############part 2######

total_size = 70000000
root_size = root_directory.size

unused_space = total_size - root_size

required_space = 30000000

target_size = required_space - unused_space
print(target_size)

best_dir = 99999999999

for current_dir in all_directory_sizes:
    if int(current_dir) > target_size and int(current_dir) < best_dir:
        best_dir = int(current_dir)

print("best directory to delete has size : ",best_dir)



