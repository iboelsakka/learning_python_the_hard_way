# Created by Ibrahim Elsakka on 4/13/2017

people = 30
cars = 40
trucks = 15

# True
if cars > people:
	print "We should take the cars."
elif cars < people:
	print "We should not take the cars."
else:
	print "We can't decide."

# False
if trucks > cars:
	print "That's too many trucks."
# True
elif trucks < cars:
	print "Maybe we could take the trucks."
else:
	print"We still can't decide."

#True
if people > trucks:
	print "Alright, let's just take the trucks."
else:
	print "Fine, let's stay home then."