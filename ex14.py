# -*- coding: utf-8 -

from sys import argv

script, user_name, user_age = argv
#prompt = "> "
popup = "=> "

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
#likes = raw_input(prompt)
likes = raw_input(popup)

print "Is your age %s %s?" % (user_age, user_name)
#likes = raw_input(prompt)
likes = raw_input(popup)

print "Where do you live %s?" % user_name
#lives = raw_input(prompt)
lives = raw_input(popup)

print "What kind of computer do you have?"
#computer = raw_input(prompt)
computer = raw_input(popup)

print """
Alright, so you said %s about liking me.
You live in %r. Not sure where that is.
And you have %r computer. Nice.
""" % (likes, lives, computer)

#用%r输出的文字会有''，要改成%s