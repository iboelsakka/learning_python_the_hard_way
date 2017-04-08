# Created by Ibrahim Elsakka on 4/7/2017

name = "Ibrahim Elsakka"
age = 20
height = 70
weight = 205
eyes = "Brown"
teeth = "White"
hair = "Brown"
pound_to_kilo_ratio = 2.205
inch_to_meter_ratio = 39.37

metric_height = height / inch_to_meter_ratio
metric_weight = weight / pound_to_kilo_ratio

print "Let's talk about %s." % name
print "He's %d inches tall, or in the metric system %.2f meters tall" % (height, metric_height)
print "He's %d pounds heavy, or in the metric system %.2f kilograms heavy" % (weight, metric_weight)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." %teeth

print "If I add %d, %d, and %d I get %d." %(age, height, weight, age + height + weight)

print "If I raise 19 to the third power, I get %E" %(19 ** 3)
print "If I raise 19 to the third power, I get %e" %(19 ** 3)
print "If I raise 19 to the third power, I get %d" %(19 ** 3)
print "If I raise 19 to the third power, I get %g" %(19 ** 3)