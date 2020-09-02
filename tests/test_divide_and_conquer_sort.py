import sys
sys.path.append('src')

from divide_and_conquer_sort import conquer_and_divide_sort

arrays = [[6,9,7,4,2,1,8,5],[6,9,7,4,2,1,8,5,7],[6,9,7,4,2,1,8,5,12,52],[6,9,7,1,8,5],[3,2],[-5,1,2,61,31,-54,71]]

for i in range(len(arrays)):
    print('Divide and Conquer Sort Test',i+1)
    print(conquer_and_divide_sort(arrays[i]))
    print('Passed')