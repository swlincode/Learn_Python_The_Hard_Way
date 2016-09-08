# -*- coding: utf-8 -

formatter = "%r %r %r %r"

#formatter = "%s %s %s %s"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)

#print formatter % ("國", "国", "龙", "龍")

print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)

print "------"
print formatter % ("one", 3, False, formatter)