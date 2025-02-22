#!/usr/bin/python
# -*- coding: utf-8 -*import

def powersum(power, *args):
    '''Return the sum of each argument raised to the specified power.'''
    total = 0
    
    for i in args:
        total += pow(i, power)
    
    return total

# ...

powersum(2, 3, 4)
powersum(2, 10)

'''
A * prefix is used on the args variable, all extra arguments passed to the function are stored in args as a tuple.
If a ** prefix is used instead, the extra parameters would be considered to be key/value pairs of a dictionary.
'''
