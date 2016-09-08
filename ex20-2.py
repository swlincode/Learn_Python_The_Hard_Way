# -*- coding: utf-8 -

from sys import argv

script, input_file = argv

def print_all(x):
	print x.read()

def rewind(x):
	x.seek(0)
	#seek是以byte為單位，如果輸入(7)，則會第7的字元開始
	
def print_a_line(line_count, x):
	print line_count, x.readline()
	#line_count只是展示行數，跟readline無關，readline是以一行為單位，讀取完一行後停止
	
def print_read_line(x):
	print x.readline()
	
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind od like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

print "*********"
print_read_line(current_file)
#這樣寫會從上一個讀取的行數接著下去

print "*********"
rewind(current_file)
print_read_line(current_file)
print_read_line(current_file)
print_read_line(current_file)
#要重新開始就要在執行一次rewind
