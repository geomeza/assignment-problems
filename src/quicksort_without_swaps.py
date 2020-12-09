def quicksort(arr, pivot_index):
    pivot = arr[pivot_index]
    del arr[pivot_index]
    less = []
    greater = []
    for num in arr:
        if num <= pivot:
            less.append(num)
        else:
            greater.append(num)
    sorted_list = []
    if len(less) > 1:
        less = quicksort(less, -1)
    if len(greater) > 1:
        greater = quicksort(greater, -1)
    if len(less) > 0:
        sorted_list.extend(less)
    sorted_list.append(pivot)
    if len(greater) > 0:
        sorted_list.extend(greater)
    return sorted_list