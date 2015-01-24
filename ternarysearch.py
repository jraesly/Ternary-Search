def ternarySearch(a,k):
	n = len(a)
	index = 0
	index1 = n//3
	index2 = (2*n)//3
	while index <= index1 and index1 <= index2 and index2 < n:
		if k <= a[index1]:
			if k == a[index]:
				return True
			else:
				index += 1
		elif a[index1] <= k <= a[index2]:
			if k == a[index2]:
				return True
			else:
				index1 += 1
		else:
			if k ==a[index2]:
				return True
			else:
				index2 += 1
	return False
