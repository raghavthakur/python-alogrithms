def binary_search(list, item):
	low = 0
	high = len(list) - 1
	
	while low <= high: # while you haven't narrowed it down to one element
		mid = (low + high) // 2 # check the middle
		guess = list[mid]

		if guess == item: # found the item
			return mid
		if guess > item: # set new high
			high = mid - 1
		else: # guess is too low, set new low
			low = mid + 1
	return None # item does not exist

my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))
print(binary_search(my_list, -1))
