# -*- coding: utf-8 -

def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b
	
def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b
	
def divide(a, b):
	print "DIVIDING %d / %d" %(a, b)
	return a / b
	
print "Let's do some math with just functions!"

age = add(30, 5)
#30 plus 5
height = subtract(78, 4)
#78 minus 4
weight = multiply(90, 2)
#90 times 2
iq = divide(100, 2)
#100 by 2

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

#def what(x, y):
#	return x + y
#result = what(age, subtract(height, multiply(weight, divide(iq, 2))))
#print "That becomes:", result, "Can you do it by hand?"

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes:", what, "Can you do it by hand?"

#>what = add(35 + subtract(height, multiply(weight, divide(iq, 2))))
#>what = add(35 + subtract(74, multiply(weight, divide(iq, 2))))
#>what = add(35 + subtract(74, multiply(180, divide(iq, 2))))
#>what = add(35 + subtract(74, multiply(180, divide(50, 2))))
#>what = add(35 + subtract(74, multiply(180, divide(50, 2))))
#>what = add(35 + subtract(74, multiply(180, 25)))
#>what = add(35 + subtract(74, 4500))
#>what = add(35 + -4426)
#>what = -4391


#練習24 + 34 / 100 - 1023

def formulaX(a1, a2, a3, a4):
	print "%d plus %d by %d minus %d" % (a1, a2, a3, a4)
	return a1 + a2 / a3 - a4

a1_input = float(raw_input("輸入24： "))
a2_input = float(raw_input("輸入34："))
a3_input = float(raw_input("輸入100："))
a4_input = float(raw_input("輸入1023："))

formulaX_result = formulaX(a1_input, a2_input, a3_input, a4_input)

print "%d" % formulaX_result
