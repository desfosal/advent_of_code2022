
import numpy as np
import matplotlib.pyplot as plt

file1 = open('input_day9.txt', 'r')
lines = file1.readlines()

stripped_lines = []
for line in lines:
  stripped_line = line.strip()
  stripped_lines.append(stripped_line)

print(stripped_lines)

test = np.zeros((2,2))
print(test)


start_row = 0
start_column = 0
number_of_segments = 10
class Snake:
    
    def __init__(self):

        #self.head_row = start_row
        #self.head_column = start_column

        self.segments = []

        for segment in range(0,number_of_segments):
            self.segments.append([start_row,start_column])
            

        self.visited_by_tail = []
        self.visited_by_tail.append([self.segments[-1][0],self.segments[-1][1]])

    def visualize(self):

        for index in range(0,number_of_segments):
            print("Segment : ",index,"Position : ",self.segments[index])

        #grid = -1*np.ones((26,26))

        #offset = 13
        #for index in range(0,9):
        #    row = self.segments[index][0]+offset
        #    col = self.segments[index][1]
         #   grid[row,col] = index
        #print(grid)

        #plt.plot(row,col,'or')

             
    

    def adjust_segments(self,direction):        

        for segment_index in range(1,number_of_segments):

            #if segment not in diagonal neighborohood of previous segment, put it behind previous segment
            horizontal_distance = (self.segments[segment_index-1][1]-self.segments[segment_index][1])
            vertical_distance = (self.segments[segment_index-1][0]-self.segments[segment_index][0])

            distance_squared = horizontal_distance**2 + (vertical_distance)**2

            if distance_squared > 2:

                #if horizontal_distance == 0:
                 #   if direction == "U":
                  #      self.segments[segment_index][0] = self.segments[segment_index -1][0] + 1
                   #     self.segments[segment_index][1] = self.segments[segment_index -1][1]
                    #elif direction == "D":
                     #   self.segments[segment_index][0] = self.segments[segment_index -1][0] - 1
                      #  self.segments[segment_index][1] = self.segments[segment_index -1][1] 


                if distance_squared == 4:

                    if vertical_distance == 2: # new feature to test.doesnt work

                        self.segments[segment_index][0] = self.segments[segment_index -1][0]-1
                        self.segments[segment_index][1] = self.segments[segment_index -1][1]

                    elif  vertical_distance == -2:
                        self.segments[segment_index][0] = self.segments[segment_index -1][0]+1
                        self.segments[segment_index][1] = self.segments[segment_index -1][1]

                    elif  horizontal_distance == 2:
                        self.segments[segment_index][0] = self.segments[segment_index -1][0]
                        self.segments[segment_index][1] = self.segments[segment_index -1][1]-1

                    elif  horizontal_distance == -2:
                        self.segments[segment_index][0] = self.segments[segment_index -1][0]
                        self.segments[segment_index][1] = self.segments[segment_index -1][1]+1


                    #match direction:

                      #  case "R":

                           # self.segments[segment_index][0] = self.segments[segment_index -1][0]
                          #  self.segments[segment_index][1] = self.segments[segment_index -1][1] - 1
                            
                            
                       # case "L":

                       #     self.segments[segment_index][0] = self.segments[segment_index -1][0]
                       #     self.segments[segment_index][1] = self.segments[segment_index -1][1] + 1
                            
                            

                       # case "U":
                        #  if horizontal_distance >= 1 and vertical_distance >= 1:
                        #     self.segments[segment_index][0] = self.segments[segment_index -1][0] + 1
                            #    self.segments[segment_index][1] = self.segments[segment_index -1][1]

                           # self.segments[segment_index][0] = self.segments[segment_index -1][0] + 1
                           # self.segments[segment_index][1] = self.segments[segment_index -1][1] 

                       # case "D":

                         #   self.segments[segment_index][0] = self.segments[segment_index -1][0] - 1
                          #  self.segments[segment_index][1] = self.segments[segment_index -1][1] 

                elif distance_squared == 5:

                    if horizontal_distance == 1 and vertical_distance == 2: #moving right and down
                        self.segments[segment_index][0] = self.segments[segment_index][0] + 1
                        self.segments[segment_index][1] = self.segments[segment_index][1] + 1
                    elif horizontal_distance == -1 and vertical_distance == 2: #moving left and down
                        self.segments[segment_index][0] = self.segments[segment_index][0] + 1
                        self.segments[segment_index][1] = self.segments[segment_index][1] - 1
                    elif horizontal_distance == 1 and vertical_distance == -2: #moving right and up
                        self.segments[segment_index][0] = self.segments[segment_index][0] - 1
                        self.segments[segment_index][1] = self.segments[segment_index][1] + 1
                    elif horizontal_distance == -1 and vertical_distance == -2: #moving left and up
                        self.segments[segment_index][0] = self.segments[segment_index][0] - 1
                        self.segments[segment_index][1] = self.segments[segment_index][1] - 1
                    
                    elif horizontal_distance == 2 and vertical_distance == 1: #moving right and down
                        self.segments[segment_index][0] = self.segments[segment_index][0] + 1
                        self.segments[segment_index][1] = self.segments[segment_index][1] + 1
                    elif horizontal_distance == -2 and vertical_distance == 1: #moving left and down
                        self.segments[segment_index][0] = self.segments[segment_index][0] + 1
                        self.segments[segment_index][1] = self.segments[segment_index][1] - 1
                    elif horizontal_distance == 2 and vertical_distance == -1: #moving right and up
                        self.segments[segment_index][0] = self.segments[segment_index][0] - 1
                        self.segments[segment_index][1] = self.segments[segment_index][1] + 1
                    elif horizontal_distance == -2 and vertical_distance == -1: #moving left and up
                        self.segments[segment_index][0] = self.segments[segment_index][0] - 1
                        self.segments[segment_index][1] = self.segments[segment_index][1] - 1
                    

                elif distance_squared == 8:

                    if horizontal_distance == 2 and vertical_distance == 2: #moving right and down
                        self.segments[segment_index][0] = self.segments[segment_index][0] + 1
                        self.segments[segment_index][1] = self.segments[segment_index][1] + 1
                    elif horizontal_distance == -2 and vertical_distance == 2: #moving left and down
                        self.segments[segment_index][0] = self.segments[segment_index][0] + 1
                        self.segments[segment_index][1] = self.segments[segment_index][1] - 1
                    elif horizontal_distance == 2 and vertical_distance == -2: #moving right and up
                        self.segments[segment_index][0] = self.segments[segment_index][0] - 1
                        self.segments[segment_index][1] = self.segments[segment_index][1] + 1
                    elif horizontal_distance == -2 and vertical_distance == -2: #moving left and up
                        self.segments[segment_index][0] = self.segments[segment_index][0] - 1
                        self.segments[segment_index][1] = self.segments[segment_index][1] - 1
                    
                    elif horizontal_distance == 2 and vertical_distance == 2: #moving right and down
                        self.segments[segment_index][0] = self.segments[segment_index][0] + 1
                        self.segments[segment_index][1] = self.segments[segment_index][1] + 1
                    elif horizontal_distance == -2 and vertical_distance == 2: #moving left and down
                        self.segments[segment_index][0] = self.segments[segment_index][0] + 1
                        self.segments[segment_index][1] = self.segments[segment_index][1] - 1
                    elif horizontal_distance == 2 and vertical_distance == -2: #moving right and up
                        self.segments[segment_index][0] = self.segments[segment_index][0] - 1
                        self.segments[segment_index][1] = self.segments[segment_index][1] + 1
                    elif horizontal_distance == -2 and vertical_distance == -2: #moving left and up
                        self.segments[segment_index][0] = self.segments[segment_index][0] - 1
                        self.segments[segment_index][1] = self.segments[segment_index][1] - 1

                else :
                    print("bleh")
                    


                        

                self.visited_by_tail.append([self.segments[-1][0],self.segments[-1][1]])

        

    def move(self,direction,distance):

        for step in range(distance):

            match direction:
                case "R":
                    self.segments[0][1] += 1
                    self.adjust_segments(direction)
                case "L":
                    self.segments[0][1] -= 1
                    self.adjust_segments(direction)
                case "U":
                    self.segments[0][0] -= 1
                    self.adjust_segments(direction)
                case "D":
                    self.segments[0][0] += 1
                    self.adjust_segments(direction)

snake = Snake()       

for line in stripped_lines:
    splitted_line = line.split(" ")

    print(splitted_line)
    direction = splitted_line[0]
    distance = int(splitted_line[1])
    snake.move(direction,distance)

    
    snake.visualize()
    print("step done")
    #print("Current row : ", snake.head_row, "Current column : ",snake.head_column)
    

print(snake.visited_by_tail)
k = snake.visited_by_tail
import itertools
k.sort()
filtered_positions = list(k for k,_ in itertools.groupby(k))

print("List after removing duplicate elements: ", filtered_positions)
#answer = np.count_nonzero(snake.visited_by_tail)
print("number of visited places : ",len(filtered_positions))