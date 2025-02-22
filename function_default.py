#!/usr/bin/python
# -*- coding: utf-8 -*-


def say(message, times = 1):
    print(message * times)


say('Hello')
say('World', 5)

# !! def func(a, b = 5) is valid, but def func(a = 5, b) is not valid. !!
