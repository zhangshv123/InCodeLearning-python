#!/usr/bin/python

import sys
def findMin(arr1,arr2):
	arr1.sort()
	arr2.sort()
	i,j=0,0
	while i<len(arr1) and j<len(arr2):
		if arr1[i]==arr2[j]:
			return arr1[i]
		elif arr1[i]<arr2[j]:
			i+=1
		else:
			j+=1
	return -1
	
arr1 = [sys.maxint]
arr2 = [sys.maxint]
print findMin(arr1,arr2)