#!/usr/bin/python
# -*- coding: utf-8 -*-

bri = set(['brazil', 'russia', 'india'])

'india' in bri
'usa' in bri
bric = bri.copy()
bric.add('china')
bric.issuperset(bri)
bri.remove('russia')
bri & bric  # OR bri.intersection(bric)
