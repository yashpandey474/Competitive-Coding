class Solution:
	# @param A : tuple of integers
	# @return an integer
	def maxProfit(self, A):
		cache = {}
		
		for index in range(len(A), -1, -1):
			for state in [True, False]:
				if index == len(A):
					cache[(index, state)] = 0
					
				else:
					#CAN BUY
					if state:
						cache[(index, state)] = max(
							#BOUGHT
							cache[(index + 1, False)] - A[index],
							cache[(index + 1, True)]
						)
						
					#CAN SELL
					else:
						cache[(index, state)] = max(
							#SOLD
							cache[(index + 1, True)] + A[index],
							cache[(index + 1, False)]
						)
			
		return cache[(0, True)]
		