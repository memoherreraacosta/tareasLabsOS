def search(array,valor):
	if len(array) == 1:
		if array[0] == valor:
			return 0
		else:
			return false
	else: 
		binarySearch(array,0,len(array)-1, valor)

def binarySearch(array, start, end, valor):
	mid = (start+end)//2

	if(array[mid]==valor):
		return mid
	elif(array[mid]>valor):
		binarySearch(array, mid+1, end, valor)
	elif(array[mid]<valor):
		binarySearch(array, start, mid-1, valor)
	else:
		return false

array = [1,2,3,4,5,6,7,8,9,10]
print(search(array,1))
print(search(array,-1))

