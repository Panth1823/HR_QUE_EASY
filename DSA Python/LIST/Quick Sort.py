def quicksort(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    return quicksort(left) + middle + quicksort(right)

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
sorted_list = quicksort(test)
print(sorted_list)