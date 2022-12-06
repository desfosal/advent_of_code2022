
file1 = open('input_day6.txt', 'r')
lines = file1.readlines()

number_of_characters = len(lines)

def detect_start_marker(list_of_chars):

    found_characters = [0 for element in range(26)] #  a to z will be 0 to 25. set to 1 if corresponding character is found
                                                    # then, if we find the same character again, we are done!

    for letter in list_of_chars:

        ascii = ord(letter)
        
        if ascii >= 97 and ascii <= 122:
            letter_position = ascii-97
    
        if found_characters[letter_position] == 1:
            return False
        else:
            found_characters[letter_position] = 1

    return True

answer = -1

message = lines[0]

marker_length = 14
for index in range(0,len(message)):
    
    current_string = message[index:index+marker_length]
    is_marker_found = detect_start_marker(current_string)
   
    if is_marker_found:
        answer = index + marker_length
        break


print("found marker : ",answer)

