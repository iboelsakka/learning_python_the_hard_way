# Created by Ibrahim Elsakka on 4/13/2017

def create_list(num_elements, increment):
	i = 0
	numbers = []
	while i < num_elements:
		print "At the top i is %d" % i
		numbers.append(i)

		i += increment
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

	print "The numbers: "
	for num in numbers:
		print num
	return numbers

def for_create_list(num_elements):
	numbers = []
	for i in range(num_elements):
		print "i is %d" % i
		numbers.append(i)
		print "Numbers now: ", numbers

	print "The numbers: "
	for num in numbers:
		print num
	return numbers

num = int(raw_input("How many numbers do you want in your list? "))
inc = int(raw_input("In increments of: "))
# my_list = create_list(num, inc)
list2 = for_create_list(num)

