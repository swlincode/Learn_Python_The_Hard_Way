# -*- coding: utf-8 -

print "How old are you?",
age = raw_input()
print "How tall are you? (cm)",
height = int(raw_input())
#int()把raw_int()變成整數
print "How much do you weight (kg)",
weight = int(raw_input())
print "So, you're %r old, %s tall and %r heavy." % ( age, height, weight )
	
#BMI公式：體重(公斤) / 身高(公尺)次方
bmi = weight / ( height * 0.01 ) ** 2
round_bmi = round ( weight / ( height * 0.01 ) ** 2 ) 
#次方的python運算是**, 2的5次方= 2**5
print "And, your BMI is %s." % bmi
print "And, your round BMI is %s." % round_bmi