from os import *
from sys import *
from collections import *
from math import *

def checkPalindrome(s):
    # Write your code here
	# Return a boolean
	st = 0
	en = len(s) - 1


	while st < en:
		if not s[st].isalpha() and not s[st].isdigit():
			st += 1
		elif not s[en].isalpha() and not s[en].isdigit():
			en -= 1
		else:
			if s[st].lower() != s[en].lower():
				return False

			st += 1
			en -= 1

	return True
