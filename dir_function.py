#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

# get names of attributes in sys module
dir(sys)

# only few entries shown here

# get names of attributes for current module
dir()

# create a new variable 'a'
a = 5
dir()

# delete/remove a name
del a
dir()

vars()  # function which can potentially give you the attributes and their values,
#  but it will not work for all cases
