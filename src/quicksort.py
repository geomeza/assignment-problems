def quicksort(arr):
    piv = 0
    i = 0
    if len(arr) == 1 or len(arr) == 0:
        return arr
    for j in range(1,len(arr)):
        if arr[j] < arr[piv]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        if j == len(arr) - 1:
            arr[piv], arr[i] = arr[i], arr[piv]
            piv = i
    lower_half = quicksort(arr[:piv])
    higher_half = quicksort(arr[piv + 1:])
    return lower_half + [arr[piv]] + higher_half
    