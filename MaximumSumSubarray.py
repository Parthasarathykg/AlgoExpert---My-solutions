def maximumSumSubmatrix(matrix, size):
	sumsList = []
    for i in range(len(matrix)-size+1):
		for j in range(len(matrix[0])-size+1):
			sums = 0
			for k in range(i,i+size):
				for l in range(j,j+size):
					sums += matrix[k][l]
			print(sumsList.append(sums))
			
	return max(sumsList)