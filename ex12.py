age = raw_input("How olds are you?")
#可以用不同方式寫：
#print "How old are you?, 
#age = raw_input()

age = raw_input()
#重複的function會被覆寫
height = raw_input("How tall are you?")
weight = raw_input("How much do you weight?")

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)