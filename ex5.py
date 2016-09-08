# -*- coding: utf-8 -

name = 'Zed'
age = 25
height_in = 74 # inches
height_cm = round(height_in * 2.54) # convert and round
weight_lbs = 180 # lbs
weight_kg = round(weight_lbs / 2.204) # convert and round
eyes = 'Blue'
teeth = 'white'
hair = 'brown'

print "Let's talk about %r." % name
print "He's %d inches tall." % height_in
print "which is %r centimeters tall." % height_cm
print "He's %d pounds heavy." % weight_lbs
print "convert to kg = %r" % weight_kg
print "actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
	age, height_in, weight_lbs, age + height_in + weight_lbs )

