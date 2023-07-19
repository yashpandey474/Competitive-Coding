from os import *
from sys import *
from collections import *
from math import *

#ALREADY SORTED MATRIX OF DENOMINATIONS
denominations = [1, 2, 5, 10, 20, 50, 100, 500, 1000]

def recursion(amount):
	#BASE CASE FOR WHEN AMOUNT REACHES 0
	if amount == 0:
		return 0

	#IF AMOUNT IS NOT REACHABLE
	if amount < 0:
		return float('inf')
		
	#INITIALLY INFINITY
	res = float('inf')
	for i in range(len(denominations)-1, -1, -1):
		if denominations[i] <= amount:
			#RECURSE FOR DEDUCTED AMOUNT 
			rec_res = recursion(amount - denominations[i])
			
			#CHOOSE MINIMUM VALUE OF RESULT BY ADDING 1 COIN TO SUB RESULT
			if rec_res != float('inf') and rec_res + 1 < res:
				res = rec_res + 1

	#RETURN THE NUMBER OF COINS
	return res

def findMinimumCoins(amount):

	# Write your code here
	return recursion(amount)
