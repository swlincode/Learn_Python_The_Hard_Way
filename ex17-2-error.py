# -*- coding: utf-8 -

from sys import argv
from os.path import exists

script, from_file, to_file = argv

indata = open(from_file).read()

print """Copying from %s to %s.
The input file is %d bytes long.
Does the output file exist? %s.
Ready, hit RETURN to continue, CTRL-C to abort.%s""" % (from_file, to_file, len(indata), exists(to_file),raw_input())
#如果把raw_input()寫在裡面，會導致一開始就pause

out_file = open(to_file, "w").write(indata)

print "Alright, all done."


