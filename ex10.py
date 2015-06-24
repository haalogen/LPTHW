# -*- coding: utf-8 -*-

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

print "ASCII bell \a"   # doesn't work in gnome-terminal  
print"lkdd\f;lkds"  # formfeed -- nextline, SAME column
print "kferf\voweifjef" # vertical tab == formfeed

print '''
Another
multiline
string
'''

while True:         # rotating stick
    for i in ["/", "-", "\\", "|"]:
        print "%s\r" % i,
