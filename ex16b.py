# Created by Ibrahim Elsakka on 4/10/2017

from sys import argv

script, filename = argv

print "This script is named %s!" % script

print "You gave me a file to read called %s" % filename
print "Opening file"
content_of_file = open(filename)

print "Here is the content of your file"
print content_of_file.read()
# Trying to read a file without resetting the pointer results in a blank line
	# being printed
# print content_of_file.read()
content_of_file.close()