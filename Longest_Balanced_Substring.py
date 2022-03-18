# My solution Brute force 
# Time complexity - O(n^3) 
# space complexity - O(n)
# Longest Balanced String 
# Difficulty - Very Hard. 

def longestBalancedSubstring(string):
	maxLength = 0
	for i in range(len(string)-1):
		for j in range(i+2,len(string)+1,2):
			if isBalanced(string[i:j]):
				if len(string[i:j]) > maxLength:
					maxLength = len(string[i:j])				
	return maxLength

def isBalanced(string):
	array = []
	for i in string:
		if i == '(':
			array.append('(')
		else:
			if len(array) > 0:
				array.pop()
			else:
				return False
	if len(array) == 0:
		return True
	else:
		return False
			
			