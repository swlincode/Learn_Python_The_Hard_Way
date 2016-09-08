# -*- coding: utf-8 -

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")
#If you hit CTRL-C is will explode, but at least it didn't keep running

print "Opening the file..."
target = open(filename, "w")
#'w' open for writing

print "Ttruncating the file. Goodbye!"
target.truncate()
#telling the file make your self zero size
#不需要這行也能繼續Writing

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
#定義3個輸入並展示文字line 1,2,3

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()
