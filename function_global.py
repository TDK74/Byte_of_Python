#!/usr/bin/python
# -*- coding: utf-8 -*-


x = 50


def func():
    global x

    print('x is', x)
    x = 2
    print('Changed global x to', x)


func()
print('Value of x is', x)

# global x, y, z  <- also possible
