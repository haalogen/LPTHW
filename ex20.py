# -*- coding: utf-8 -*-
from sys import argv

script, input_file = argv

def print_all(f):
    txt = f.read()
    print txt
    print "Length of text: ", len(txt)

def rewind(f):
    print "Old position in file: ", f.tell()
    f.seek(0)
    print "New position in file: ", f.tell()

def print_a_line(line_count, f):
    print line_count, f.readline(),

current_file = open(input_file)


print "First let's print the whole file:\n"
print_all(current_file)

print "Now let's rewind, kind of like tape."
rewind(current_file)


print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

