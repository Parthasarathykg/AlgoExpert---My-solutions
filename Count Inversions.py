# Count Inversion - very Hard 

def countInversions(array):
	countInversionArray = []
	for i in range(len(array)):
		for j in range(i+1, len(array)):
			if array[j] < array[i]:
				countInversionArray.append([i,j])
	return len(countInversionArray)
def swap(array,i,j):
	array[i],array[j] = array[j],array[i]
	return array
		

