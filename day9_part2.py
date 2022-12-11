
import numpy as np

file1 = open('input_day9_small_part2.txt', 'r')
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

class Snake:
    
    def __init__(self):

        #self.head_row = start_row
        #self.head_column = start_column

        self.segments = []

        for segment in range(0,9):
            self.segments.append([start_row,start_column])
            

        self.visited_by_tail = []
        self.visited_by_tail.append([self.segments[-1][0],self.segments[-1][1]])
    

    def adjust_segments(self,direction):        

        for segment_index in range(1,9):

            #if segment not in diagonal neighborohood of previous segment, put it behind previous segment
            if (self.segments[segment_index-1][1]-self.segments[segment_index][1])**2 + (self.segments[segment_index-1][0]-self.segments[segment_index][0])**2 > 2:

                match direction:

                    case "R":

                        self.segments[segment_index][0] = self.segments[segment_index -1][0]
                        self.segments[segment_index][1] = self.segments[segment_index -1][1] - 1
                        
                        
                    case "L":

                        self.segments[segment_index][0] = self.segments[segment_index -1][0]
                        self.segments[segment_index][1] = self.segments[segment_index -1][1] + 1
                        
                        

                    case "U":

                        self.segments[segment_index][0] = self.segments[segment_index -1][0] + 1
                        self.segments[segment_index][1] = self.segments[segment_index -1][1] 

                    case "D":

                        self.segments[segment_index][0] = self.segments[segment_index -1][0] - 1
                        self.segments[segment_index][1] = self.segments[segment_index -1][1] 

                        

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
    direction = splitted_line[0]
    distance = int(splitted_line[1])
    snake.move(direction,distance)
    #print("Current row : ", snake.head_row, "Current column : ",snake.head_column)
    

print(snake.visited_by_tail)
k = snake.visited_by_tail
import itertools
k.sort()
filtered_positions = list(k for k,_ in itertools.groupby(k))

#print("List after removing duplicate elements: ", filtered_positions)
#answer = np.count_nonzero(snake.visited_by_tail)
print("number of visited places : ",len(filtered_positions))