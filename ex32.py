# Created by Ibrahim Elsakka on 4/13/2017

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
	print "This is count %d" % number

for fruit in fruits:
	print "A fruit of type: %s" % fruit

for i in change:
	print "I got %r" % i

elements = []

# with one argument, goes from 0 to arg - 1
# with two arguments, goes from arg1 to arg2 - 1
# with three arguments, goes from arg1 to arg2 - 1 in increments of arg3
	# NOTE ALL PARAMETERS MUST BE INTEGERS
# for i in range(1, 6):
# 	print "Adding %d to the list." % i
# 	elements.append(i)

elements = range(0, 6)


for i in elements:
	print "Element was: %d" % i