from grammar import *

g = Grammar("sample.txt")

for _ in xrange(10):
    print g.generate()
