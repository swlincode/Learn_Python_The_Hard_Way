#print "I am 6'2\" tall."
#print 'I am 6\'2" tall.'

#print "I am 6\'2\" tall." 
#print 'I am 6\'2\" tall.'


tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat


formatter = "%s, %s, %s, %s"
#Do not use %r.Always remember this: %r is for debugging, %s is for displaying.

print formatter % ("\'", "\"", "\\", "\n")