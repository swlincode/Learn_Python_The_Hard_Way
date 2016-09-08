# -*- coding: utf-8 -

from sys import argv
from os.path import exists

script, from_file, to_file = argv

indata = open(from_file).read()

print """Copying from %s to %s.
The input file is %d bytes long.
Does the output file exist? %s.
Ready, hit RETURN to continue, CTRL-C to abort.""" % (from_file, to_file, len(indata), exists(to_file))
#本想把raw_input()寫在print的最後，但這樣會導致一開始就暫停...

raw_input()

out_file = open(to_file, "w").write(indata)
#這樣寫就不需要在最後執行out_file.close()，python會自動關閉

print "Alright, all done."


