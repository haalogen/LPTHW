#-*- coding:utf-8 -*-
""" LPTHW - ex33 - While Loops"""

def append_numbers(numbers, num, step):
    """This function appends int numbers [0, 1, 2 ... num -1] to the passed list numbers."""
    if step <= 0:
        print "Infinite Loop: step == ", step
        return
    i = 0
    while i < num:
        print "At the top i is %d" % i
        numbers.append(i)
        
        i += step
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i


numbers = []

append_numbers(numbers, 10, 3)

print "The numbers:"

for num in numbers:
    print num
