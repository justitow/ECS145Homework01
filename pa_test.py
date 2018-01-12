import ProblemA

a = ProblemA.polynom([1, 2])
b = ProblemA.polynom([3, 4])

print "Test of basic addition"
print a + b

c = ProblemA.polynom([1, 2, 3])

print "Test of singular difference"
print a + c
print c + a

print "test of large difference"
d = ProblemA.polynom([1, 1, 1, 1, 1, 1, 1, 1])
print a + d
print d + a

e = ProblemA.polynom([1])

print c + e
print e + c

f = ProblemA.polynom([])

print f + d
print d + f

g = ProblemA.polynom([0, 2, 3, 0])
print g.poly

h = ProblemA.polynom([0, 0, 0, 2, 0, 3])
print h.poly

i = ProblemA.polynom([0])
j = ProblemA.polynom([0, 0])
k = ProblemA.polynom([0, 0, 0])

print i.poly, j.poly, k.poly

print a - b
print b - a

print a - c
print c - a
