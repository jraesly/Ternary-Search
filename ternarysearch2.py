def ternarySearch(a,k):
	n = len(a)
	index = 0
	index1 = (n)//3
	index2 = (2*n)//3
	if n == 0:
		return False
	if a[index1] == k or a[0] == k or a[index2] == k or a[n-1] == k:
		return True
	elif k < a[index1]:
		return ternarySearch(a[0:index1-1], k)
	elif k > a[index2]:
		return ternarySearch(a[index2+1:n], k) 
	elif a[index1] < k < a[index2]:
		return ternarySearch(a[index1:index2], k)
	else:
		return False
	return True


# test the function by putting in new values for k
print(ternarySearch([1,3,5,10,12,15,32,91,125,132], 10000))


