#!/usr/bin/python
# -*- coding: utf-8 -*-

from mymodule import say_hi, __version__

say_hi()
print('Version', __version__)

# from mymodule import *
# This will import all public names such as say_hi but would not import __version__
# because it starts with double underscores.
