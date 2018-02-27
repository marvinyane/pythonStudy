#! /usr/bin/env python

class Base(object):
    def __init__(self):
        print "create Base"

    def visit_Base():
        print "visit base"

class A(Base):
    def __init__(self):
        print "create A"
        super(A, self).__init__()

class B(Base):
    def __init__(self):
        print "create B"
        super(B, self).__init__()

class Visitor(object):
    def visit(self, node):
        for cls in node.__class__.__mro__:
            print cls.__name__

if __name__ == "__main__":
    v = Visitor()
    a = A()
    b = B()

    v.visit(a)
    v.visit(b)
