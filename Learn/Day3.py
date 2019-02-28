#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Python 类


class MyClass:

    def __init__(self, name='无名氏', age=18):
        self.name = name
        self.age = age

    def bio(self):
        print(self.name, " ", self.age)


my = MyClass()
my.bio()

fruit = ("apple", "banana", "cherry")
fruit_ite = iter(fruit)
next(fruit_ite)
print(fruit_ite.__next__())
