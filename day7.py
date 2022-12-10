file1 = open('input_day7.txt', 'r')
lines = file1.readlines()

class TreeNode: 

    children = []
    size = 0

    def __init__(self, address, parent = None):
        self.address = address
        self.parent = parent

    def add_file_size(self,file_size):
        self.size = self.size + file_size
        self.parent.add_file_size(file_size)    



root_directory = TreeNode("/")
currentDirectory = root_directory

for line in lines[0:10]:

    print(line)
    line_contents = line.split(" ")

    if (line_contents[0].isnumeric(),int):
        print(line_contents[0])


