# -*- coding: utf-8 -

def bmi_formula(weight, height):
	return weight / ( height * 0.01 ) ** 2
	#return round(weight / ( height * 0.01 ) ** 2)

print "How tall are you? (cm)",
#height = int(raw_input())
#用int無法輸入浮點數，例如175.99，會報錯
height = float(raw_input())

print "How much do you weight (kg)",
#weight = int(raw_input())
weight = float(raw_input())

result = bmi_formula(weight, height)

print """So, you're %s tall and %r heavy.
And, your BMI is %d.""" % (height, weight, result)
