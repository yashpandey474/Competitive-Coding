from os import *
from sys import *
from collections import *
from math import *

def matrixMultiplication(arr, n):
	# Write your code here.

	cache = {}

	def dfs(m1, m2):
		if (m1, m2) in cache:
			return cache[(m1, m2)]

		if m1 == m2:
			return 0

		#FIND THE MIN COST
		min_cost = float('inf')
		for i in range(m1, m2):
			min_cost = min(
				min_cost,
				dfs(m1, i) + dfs(i + 1, m2) + arr[i]*arr[m1-1]*arr[m2]
			)

		cache[(m1, m2)] = min_cost
		return min_cost

	return dfs(1, n-1)
