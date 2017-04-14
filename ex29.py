# Created by Ibrahim Elsakka on 4/13/2017

people = 20
cats = 30
dogs = 15

# True, will execute
if people < cats:
	print "Too many cats! The world is doomed!"

# False, will not execute
if people > cats:
	print "Not many cats! The world is saved!"

# False, will not execute
if people < dogs:
	print "The world is drooled on!"

# True, will execute
if people > dogs:
	print "The world is dry!"

# dogs == 20
dogs += 5

# True, will execute
if people >= dogs:
	print "People are greater than or equal to dogs."

# True, will execute
if people <= dogs:
	print "People are less than or equal to dogs."

# True, will execute
if people == dogs:
	print "People are dogs."