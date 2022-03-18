# Smallest substring containg
# My solution but worst time complexity and space complexity
# Need to check the solution from Clement

def smallestSubstringContaining(bigString, smallString):
	subString = generateSubString(bigString,len(smallString))
	
	fMapArray = []
	
	for i in subString: 
		frequencyMap = {} 
		for j in i:
			if j not in frequencyMap:
				frequencyMap[j] = 1
			else:
				frequencyMap[j] += 1
		fMapArray.append(frequencyMap)		
	
				
	sSfrequencyMap = {}
	for i in smallString:
		if i not in sSfrequencyMap:
			sSfrequencyMap[i] = 1
		else:
			sSfrequencyMap[i] += 1
	
	setString = set()
	for i in smallString:
		setString.add(i)
	
	minlength = 999999
	minString = ''
	for i in range(len(fMapArray)):
		count = 0
		for j in setString:
			if j not in fMapArray[i]:
				break
			if sSfrequencyMap[j] <= fMapArray[i][j]:
				count += 1
		
		if count >= len(sSfrequencyMap):
			if len(subString[i]) < minlength:
				minlength = len(subString[i])
				minString = subString[i]
	return minString		
			
def generateSubString(bigString, length):
	subString = []
	for i in range(len(bigString)):
		for j in range(i+length,len(bigString)+1):
			subString.append(bigString[i:j])
	return subString
			

