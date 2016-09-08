# -*- coding: utf-8 -
#試著用ex17的例子套用def

from os.path import exists

def replace_file(from_file, to_file):
	indata = open(from_file).read()
	#print "1: %r, 2: %r" % (from_file, to_file)
	#不需要print
	print """Copying from %s to %s.
	The input file is %d bytes long.
	Does the output file exist? %s.
	Ready, hit RETURN to continue, CTRL-C to abort.""" % (from_file, to_file, len(indata), exists(to_file))

	raw_input()

	out_file = open(to_file, "w").write(indata)

	print "Alright, all done."

replace_file(raw_input("輸入原始檔案名稱"), raw_input("輸入新的檔案名稱"))
#讓user自己輸入from_file, to_file的名稱