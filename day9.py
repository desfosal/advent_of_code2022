
import numpy as np

file1 = open('input_day9.txt', 'r')
lines = file1.readlines()

stripped_lines = []
for line in lines:
  stripped_line = line.strip()
  stripped_lines.append(stripped_line)

print(stripped_lines)

test = np.zeros((2,2))
print(test)

#grid_length = 1200
#grid = np.zeros((grid_length,grid_length))

start_row = 0
start_column = 0

class Snake:
    
    def __init__(self):

        self.head_row = start_row
        self.head_column = start_column
        self.tail_row = start_row
        self.tail_column = start_column

        self.visited_by_tail = []
        self.visited_by_tail.append([self.tail_row,self.tail_column])
    

    def adjust_tail(self,direction):

        #if tail not in diagonal neighborohood of head, put it behind the head
        if (self.head_column-self.tail_column)**2 + (self.head_row-self.tail_row)**2 > 2:

            match direction:

                case "R":
                    
                    self.tail_column = self.head_column - 1
                    self.tail_row =  self.head_row
                    
                case "L":
                    
                    self.tail_column = self.head_column + 1
                    self.tail_row =  self.head_row

                case "U":

                    self.tail_column = self.head_column 
                    self.tail_row =  self.head_row + 1

                case "D":
                    self.tail_column = self.head_column 
                    self.tail_row =  self.head_row - 1

            self.visited_by_tail.append([self.tail_row,self.tail_column])

        

    def move(self,direction,distance):

        for step in range(distance):

            match direction:
                case "R":
                    self.head_column += 1
                    self.adjust_tail(direction)
                case "L":
                    self.head_column -= 1
                    self.adjust_tail(direction)
                case "U":
                    self.head_row -= 1
                    self.adjust_tail(direction)
                case "D":
                    self.head_row += 1
                    self.adjust_tail(direction)

snake = Snake()       

for line in stripped_lines:
    splitted_line = line.split(" ")
    direction = splitted_line[0]
    distance = int(splitted_line[1])
    snake.move(direction,distance)
    print("Current row : ", snake.head_row, "Current column : ",snake.head_column)
    

#print(snake.visited_by_tail)
k = snake.visited_by_tail
import itertools
k.sort()
filtered_positions = list(k for k,_ in itertools.groupby(k))

#print("List after removing duplicate elements: ", filtered_positions)
#answer = np.count_nonzero(snake.visited_by_tail)
print("number of visited places : ",len(filtered_positions))