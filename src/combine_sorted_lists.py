def combine_sorted_lists(arrays):
    i = 0
    j = 0
    first = len(arrays[0])
    second = len(arrays[1])
    sorted = []
    while i < first and j < second:
        if arrays[0][i] < arrays[1][j]:
            sorted.append(arrays[0][i])
            i+= 1
        else:
            sorted.append(arrays[1][j])
            j+=1
    if i == first:
        sorted = sorted + arrays[1][j:]
    elif j == second:
        sorted = sorted + arrays[0][i:]
    return sorted

    