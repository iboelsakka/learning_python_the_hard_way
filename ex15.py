# Created by Ibrahim Elsakka on 4/8/2017

# imports the argv module from the sys library
from sys import argv

# stores the arguments after the python command in terminal into script and filename
script, filename = argv

# assigns the name of the file in the variable txt
txt = open(filename)

print "Here's your file %r:" % filename
# prints out the content of the txt file
print txt.read()
txt.close()

print "Type the filename again:"
# stores the name of the file the user supplies in the variable file_again
file_again = raw_input("> ")

# assigns the name of the file to the txt_again variable
txt_again = open(file_again)

# prints the content of the txt_again file
print txt_again.read()
txt_again.close()