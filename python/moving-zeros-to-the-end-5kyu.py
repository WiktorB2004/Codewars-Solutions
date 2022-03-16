import re
def move_zeros(array):
    for char in array:
        if char == 0:
            array.remove(char)
            array.append(0)         
    return array
