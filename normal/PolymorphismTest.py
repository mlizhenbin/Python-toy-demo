#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Parent:  # 定义父类
    def myMethod(self):
        print '调用父类方法'


class Child(Parent):  # 定义子类
    def myMethod(self):
        print '调用子类方法'


c = Child()  # 子类实例
c.myMethod()  # 子类调用重写方法


# !/usr/bin/python

class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print v1 + v2
