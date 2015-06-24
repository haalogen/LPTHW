# -*- coding: utf-8 -*-
from sys import argv

script, filename = argv
txt = open(filename, 'a+')

print txt.tell()
#print txt.read()

indata = raw_input("Insert text:\n")

txt.write(indata)

print txt.tell()

txt.seek(0)
print txt.read()
