from os import *
from sys import *
from collections import *
from math import *

def maximumValue(items, n, w):

	# Write your code here.
	# ITEMS contains [weight, value] pairs.
	current = 0
	items = sorted(items, key = lambda x: x[1]/x[0], reverse = True)
	total = 0

	for i in range(len(items)):
		if current + items[i][0] <= w:
			current += items[i][0]
			total += items[i][1]

		else:
			rem = w - current
			current = w
			total += (items[i][1]*rem)/items[i][0]

	return total


		


		
