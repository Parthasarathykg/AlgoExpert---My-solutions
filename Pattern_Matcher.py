# Solved by myself.
# Need to be optimized 

# Pattern Matcher without any built-in methods.

def patternMatcher(pattern, string):
	isYchanged = False
	if pattern[0] == 'y':
		isYchanged = True
		pattern = patternChanger(pattern)
	xyCountMap = findXyCount(pattern)	
	yPos = findYPos(pattern)
	
	if 'y' not in xyCountMap:
		if isYchanged:
			return ['', string[0:len(string)//xyCountMap['x']]]
		else:
			return [string[0:len(string)//xyCountMap['x']],'']
	else:
		for i in range(1,len(string)):
			x = i
			totalX = xyCountMap['x'] * i
			totalY = len(string) - totalX
			y = totalY // xyCountMap['y']
			if y < 0:
				break	
			for j in yPos:
				stringX = string[0:i]
				stringY = string[j*i:y+j*i]
				stringNew = []
				for n in pattern:
					if n == 'x':
						stringNew.append(stringX)
					else:
						stringNew.append(stringY)
				newString = ''.join(stringNew)
				
				if newString == string:
					if isYchanged:
						return([stringY,stringX])
					return ([stringX, stringY])

	return []
	
		
def findYPos(pattern):
	yPos = []
	for i in range(len(pattern)):
		if pattern[i] == 'y':
			yPos.append(i)
	return yPos
	
def findXyCount(pattern):
	xyCountMap = {}
	for i in pattern:
		if i == 'x': 
			if i not in xyCountMap:
				xyCountMap[i] = 1
			else:
				xyCountMap[i] += 1 
		else:
			if i not in xyCountMap:
				xyCountMap[i] = 1
			else:
				xyCountMap[i] += 1 
	return xyCountMap
	
def patternChanger(pattern):
	array = [''] * len(pattern)
	
	for i in range(len(pattern)):
		if pattern[i] == 'x':
			array[i]= 'y'
		elif pattern[i] == 'y':
			array[i]= 'x'
	pattern = ''.join(array)
	
	return pattern
			

