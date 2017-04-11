# Created by Ibrahim Elsakka on 4/10/2017

from sys import argv
from os.path import exists

script, from_file, to_file = argv

# print "Copying from %s to %s" % (from_file, to_file)

# we could combine these two lines by adding .read() at the end
#in_file = open(from_file).read()
# indata = in_file.read()

# print "The input file is %d bytes long" % len(indata)

# print "Does the output file exist? %r" %exists(to_file)
# print "Ready, hit RETURN to continue, CTRL-C to abort."
# raw_input()

#out_file = open(to_file, 'w').write(in_file)
# out_file.write(indata)

# With this single line of code, we read the source file and write it to the 
	# destination file.
out_file = open(to_file, 'w').write(open(from_file).read())

# print "Alright, all done."

#out_file.close()
#in_file.close()