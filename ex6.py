# Created by Ibrahim Elsakka on 4/7/2017
# this line stores the value "There are 10 types of people." in the variable x
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
# this line stores the value "Those who know binary and those who don't" in the variable y
y = "Those who know %s and those who %s." % (binary, do_not)

# prints "There are 10 types of people."
print x
# prints "Those who know binary and those who don't"
print y

# uses the %r format character to print the value stored in x with quotes
#	"I said :'There are 10 types of people.'"
print "I said :%r." % x
# uses the %s format character to print the value stored in y without quotes. Note that the %s format character
#	is enclosed with single quotes, so they appear in the output
print "I also said: '%s'." % y

hilarious = False
# stores the text with an expectation of a string variable when output to screen
joke_evaluation = "Isn't that joke so funny?! %r"

# prints the variable joke_evaluation passing in the value of hilarious, False
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

# prints the concatenation of the e string on the right side of the w string
print w + e