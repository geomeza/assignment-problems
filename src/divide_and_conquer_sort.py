from combine_sorted_lists import combine_sorted_lists

array = [6,9,7,4,2,1,8,5,7]

def split(array):
    if len(array) <= 1:
        return array
    else:
        return [array[:len(array)//2], array[len(array)//2:]]

def divide(array):
        if len(array) <= 1:
            return [array]
        else:
            parts = split(array)
            return divide(parts[0]) + divide(parts[1])

def conquer(array):
    if len(array) > 1:
        combined = []
        length = len(array)
        for i in range(len(array)):
            if i % 2 == 0:
                if i < len(array) - 1:
                    combined.append(combine_sorted_lists([array[i],array[i+1]]))
        length_comb = len(combined)
        last_elem = combined[length_comb - 1]
        if length % 2 == 1:
            combined.append(combine_sorted_lists([last_elem,array[length - 1]]))
            combined.remove(last_elem)
        return conquer(combined)
    else:
        return array

def conquer_and_divide_sort(array):
    divided = divide(array)
    conquered = conquer(divided)
    for elem in conquered:
        return elem