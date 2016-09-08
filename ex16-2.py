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
#'w' open for writeing

print "Ttruncating the file. Goodbye!"
target.truncate() 
#telling the file make your self zero size  
#不需要這行也能繼續Writing

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
#定義3個輸入並展示文字line 1,2,3

lineX = """%s \n%s \n%s\n
""" % (line1, line2, line3)
#把line123輸入的文字定義為lineX, \n換行

print "I'm going to write these to the file."

target.write(lineX)
 #寫入linex的內容

print "And finally, we close it."
target.close()
