#!/usr/bin/env python 
import sys
for line in sys.stdin:
    	line = line.strip().replace(".","")
	keys = [int(i) for i in line]
	for key in keys:
		value = 1
		print('{0}\t{1}'.format(key, value) )

