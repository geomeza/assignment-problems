def binary_search(wanted_element, sorted_list):
    mid_index = len(sorted_list)//2
    mid_element = sorted_list[mid_index]
    if mid_element == wanted_element:
        return mid_index
    else:
        if mid_element > wanted_element:
            return binary_search(wanted_element, sorted_list[:mid_index])
        else:
            return binary_search(wanted_element, sorted_list[mid_index:])

print(binary_search(7, [2, 3, 5, 7, 8, 9, 10, 11, 13, 14, 15, 16]))