#Brute force approach - Used powerset to find out all the combinations
def knapsackProblem(items, capacity):
	subset = [[]]
    for i in items:
		for j in range(len(subset)):
			currentSubset  =  subset[j]
			subset.append(currentSubset + [i])

	maxValue = 0
	newSet = []
	for i in subset:
		sums = 0
		value = 0
		for j in i:
			sums += j[1]
			value += j[0]
		if capacity >= sums and value > maxValue:
			maxValue = value
			newSet = i
			print(maxValue)
	#print([maxValue, replaceWithIndex(newSet,items)])
	return [maxValue, replaceWithIndex(newSet,items)]

def replaceWithIndex(Set,items):
	for i in range(len(Set)):
		Set[i] = items.index(Set[i])
	return Set