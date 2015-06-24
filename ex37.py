#-*- coding:utf-8 -*-
import sys

global glob_var

print "%g%%" % 10.34

@classmethod

e = {'x' : 1, 'y' : 2}
print e

print "lkfjd\vkjdhfffs"


s = lambda y: y ** y
print s(1), s(2), s(3)


with open("out.txt", 'a') as f:
    f.write("Hi there!")


a = [-1, 1, 6.6, 33, 333, 1234.5]

print "a: ", a


print "del a[0]"
del a[0]

print "a: ", a

print "del a[2:4]"
del a[2:4]

print "a: ", a

print "del a"
del a

glob_var = 0

while True:
    try:
        prompt = "Please enter a number: "
        x = int(raw_input(prompt))
        break
#    except ValueError:
#        print "Oops! That was not a valid number. Try again..."
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise
    finally:
        print 42
        
exec("print 'hello' ")




