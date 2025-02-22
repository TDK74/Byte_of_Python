#!/usr/bin/python
# -*- coding: utf-8 -*-


class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, my name is', self.name)


p = Person("My Name")
p.say_hi()
# The previous 2 lines can also be written as
# Person('My Name').say_hi()
