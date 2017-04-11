# Created by Ibrahim Elsakka on 4/7/2017

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print "printing with %r " % fat_cat
print "printing with %s " % fat_cat

# while True:
# 	for i in ["/","-","|","\\","|"]:
# 		print "%s\r" % i,