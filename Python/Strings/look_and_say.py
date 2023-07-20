def recurse(n, a):
	if n == 1:
		return a

	#ITERATE THROUGH STRING; STORING NUMBER OF SAME CHARACTERS AT EACH POINT
	counter = 0
	result = ""
	for i in range(len(a)):
		counter+=1
		if i == len(a) - 1 or a[i] != a[i+1]:
			result = result + str(counter) + a[i]
			counter = 0

	return recurse(n-1, result)

def lookAndSequence(n):
	# Write your code here.
	a = "1"
	return recurse(n,a)
	
