import sys
sys.path.append('src')

from combine_sorted_lists import combine_sorted_lists

sorted_arrays = [[[1,3,4,5,7],[2,6]], [[1,5,8,9,12],[4,5,9,20]], [[2,2,2,2,2],[2,2,2,2]], [[1,2,3,4,5,6],[2,3,4]]]

for i in range(len(sorted_arrays)):
    print('Test',i+1)
    print(combine_sorted_lists(sorted_arrays[i]))