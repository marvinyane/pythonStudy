#!usr/bin/python3

import shape

a = shape.Point()

print(repr(a))

b = shape.Point(3,4)

print(str(b))

print("{0}".format(b.distance_from_origin()))

b.x = -19
print(str(b))

p = shape.Point(28, 45)
c = shape.circle(5, 28, 45)

print(p.distance_from_origin())

print(c.distance_from_origin())

