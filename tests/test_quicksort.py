import sys
sys.path.append('src')
from quicksort import quicksort

tester = [5,8,-1,9,10,3.14,2,0,7,6]

sorted_list = quicksort(tester)

assert sorted_list == [-1, 0, 2, 3.14, 5, 6, 7, 8, 9, 10]

print('Passed')