# find the smallest element in the given array
def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i] # set new smallest
            smallest_index = i
    return smallest_index

# selection sort runtime is O(n^2)
# sort the given array in increasing order
def selectionSort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr) # finds the smallest element in the array
        new_arr.append(arr.pop(smallest)) # and add it to new array
    return new_arr

print(selectionSort([5, 3, 6, 2, 10]))
print(selectionSort([400, 2, -1, 6, 90, 1000, -30]))
print(selectionSort([-1, -5, -3, -2, 0]))
