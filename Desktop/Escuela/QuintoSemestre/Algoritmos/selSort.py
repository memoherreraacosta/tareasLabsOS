def sort(array):	
	for i in range(len(array)-1):
		minIndex = i
		for j in range(i+1, len(array)):
			if (array[j]<array[minIndex]):
				minIndex = j

		if (minIndex != i) :
			array[i] ,array[minIndex] = array[minIndex] , array[i]
	return array

array = [1,-4,-5,6,-6,4,39,28,-3,45,603,75,213,-405,5,-9000]
print(array)
print(sort(array))		
