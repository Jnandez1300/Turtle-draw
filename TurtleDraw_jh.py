# TurtleDraw_jh
# By: Julian Hernandez
#
# All rights reserved.

import turtle

TEXTFILENAME = 'turtle-draw.txt'

print('TurtleDraw')
print('Reading a text file by line')

window = turtle.Screen()
window.setup(width=450, height=450)

turtle.speed("fastest")


file= input("Enter the name of the input file: ")

try:
    # Open the input file
    with open(TEXTFILENAME, 'r') as file:
        # Read the file line by line
        for line in file:
            # Strip white space from each line

            line = line.strip()

            pieces = line.split()

            print(pieces)
except FileNotFoundError:
    print("File not found.")


    
            






turtle.done()

