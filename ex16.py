# -*- coding: utf-8 -*-
from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w+')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print "I'm going to write these to the file."

out_str = "%s\n%s\n%s\n" % (line1, line2, line3)
target.write(out_str)

target.seek(0)

print target.read()

print "And finally, we close it."
target.close()
