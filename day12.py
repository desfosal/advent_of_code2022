from advent_tools import *

import numpy as np

stripped_lines = read_lines("input_day12_small.txt")

elevations = np.zeros((len(stripped_lines),len(stripped_lines[0])))

start_position = []

for line_number,line in enumerate(stripped_lines):
    print(line)

    for position,character in enumerate(line):
        if character == "S":
            start_position = [line_number,position]
            elevations[line_number,position] = 0
        elif character == "E":
            end_position = [line_number,position]
            elevations[line_number,position] = 25
        else:
            ascii = ord(character)
            elevation = ascii-97
            elevations[line_number,position] = elevation

print(elevations)

def fill_distance_map(elevations,start_position,end_position):

    distance_map = 999*np.ones(np.size(elevations))

    distance_map[end_position] = 0

    neighbors = [[end_position[0]+1,end_position[1]],[end_position[0]-1,end_position[1]][end_position[0],end_position[1]+1],[end_position[0],end_position[1]-1]]

    visited = np.zeros(np.size(elevations))

    visited[end_position[0],end_position[1]] = 1
    
    iteration = 0
    while distance_map[start_position[0],start_position[1]] == 999 and iteration <1:

        iteration += 1
        new_neighbors = []

        for neighbor in neighbors:

            if True:
                print("test") # rendu ici si continue good algo

    return distance_map 


def fill_distance_map_slow_algorithm(elevations,start_position,end_position):

    distance_map = 999*np.ones(np.size(elevations))

    distance_map[end_position] = 0

    did_something = True

    while did_something:

        did_something = False

        for line_number in len(elevations):
            for column_number in len(elevations[0]):

                current_distance = #rendu ici si continue bad algo



