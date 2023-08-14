from os import *
from sys import *
from collections import *
from math import *

def countWays(n):
	# Write your code here.
	cache = {}

	def dfs(steps, curr):
		if steps == n:
			return 1

		if (steps, curr) in cache:
			return cache[(steps, curr)]

		if curr == "O":
			if steps == n-1:
				return 0
			
			res = (
				dfs(steps + 1, "X")+
				dfs(steps + 1, "Y")+
				dfs(steps + 1, "Z")
			)

		else:
			if steps == n - 1:
				return 1
			res = (
				dfs(steps + 1, "O")+
				dfs(steps + 1, "Y")+
				dfs(steps + 1, "Z")
			)
			
		cache[(steps, curr)] = res%(10**9 + 7)
		return res%(10**9 + 7)

	return dfs(0, "O")
