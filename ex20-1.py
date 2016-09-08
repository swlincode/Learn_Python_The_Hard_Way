# -*- coding: utf-8 -

from sys import argv

script, input_file = argv
#從argv中unpack一個變量名values script是要要執行的py，input_file是要輸入的檔案

def print_all(f):
	print f.read()
	#定義函數{function} print_all給一個參數{variable} f
	#
	
def rewind(f):
	f.seek(0)
	
def print_a_line(line_count, f):
	print line_count, f.readline()
	
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind od like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)