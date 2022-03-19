#O(n^2) Time Space O(n) Space
def largestRectangleUnderSkyline(buildings):
    # Write your code here.
	maxArea = 0
	buildingsMap = {}
	for i in range(len(buildings)):
		count = 1
		for j in range(i+1,len(buildings)):
			if buildings[j] >= buildings[i]:
				count += 1
			if buildings[j] < buildings[i]:
				break	
		print(buildings[i], count)
		if buildings[i] not in buildingsMap:
			buildingsMap[buildings[i]] = count
		else:
			continue

	for i in reversed(range(len(buildings))):
		count = 1
		for j in range(i-1,-1,-1):
			if buildings[j] >= buildings[i]:
				count += 1
			if buildings[j] < buildings[i]:
				break	
		if buildings[i] in buildingsMap and count > buildingsMap[buildings[i]]:
			buildingsMap[buildings[i]] = count
		else:
			continue

	print(buildingsMap)
	
	maxArea = 0
	for key,values in buildingsMap.items():
		if maxArea < key*values:
			maxArea = key*values
	return maxArea


