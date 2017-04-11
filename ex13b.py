# Created by Ibrahim Elsakka on 4/8/2017

from sys import argv

script, name, age = argv

print "The name of the script is:", script
print "Your name is:", name
print "You are %s years old" % age

weight = raw_input("How much do you weigh? ")
print "So, you're %s pounds heavy" % weight