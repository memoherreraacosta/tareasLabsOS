def sort(array):
	for i in range(1, len(array)):
		j = i-1
		while ( (array[j]>array[j+1]) and j>=0 ):
			array[j], array[j+1] = array[j+1] , array[j]
			j -= 1 
	return array
array = [1,-4,54,34,-23]
print(sort(array))

