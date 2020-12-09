
def is_valid(arr):
    col_one = 0;
    col_two = 0;
    col_three = 0;
    diags = 0
    reverse_diags = 0;
    for i in range(3):
        if None in arr[i]:
            return False
        if sum(arr[i]) != 15:
            return False
        col_one += arr[i][0]
        col_two += arr[i][1]
        col_three += arr[i][2]
        if arr[i][i] is not None:
            diags += arr[i][i]
        else:
            return False
    if diags != 15 or col_one != 15 or col_two != 15 or col_three != 15:
        return False
    if (arr[0][2] + arr[1][1] + arr[2][0]) != 15:
        return False
    return True

def is_currently_valid(arr):
    columns = []
    for i in range(len(arr)):
        columns.append([])
        for j in range(len(arr[0])):
            columns[i].append(arr[j][i])
    for i in range(3):
        if None in arr[i]:
            continue
        if sum(arr[i]) != 15:
            return False
    if None not in columns[0]:
        if sum(columns[0]) != 15:
            return False
    if None not in columns[1]:
        if sum(columns[1]) != 15:
            return False
    if None not in columns[2]:
        if sum(columns[2]) != 15:
            return False
    if None not in [arr[0][0], arr[1][1], arr[2][2]]:
        if sum([arr[0][0], arr[1][1], arr[2][2]]) != 15:
            return False
    if None not in [arr[0][2], arr[1][1], arr[2][0]]:
        if (arr[0][2] + arr[1][1] + arr[2][0]) != 15:
            return False
    return True

def check_completion(arr):
    all_nums = all_nums_in_arr(arr)
    if len(all_nums) < 9:
        return False
    else:
        return is_valid(arr)

def all_nums_in_arr(arr):
    all_nums = []
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] is not None:
                all_nums.append(arr[i][j])
    return all_nums

def solve_square(square):
    for i in range(9):
        row = i//3
        col = i%3
        if square[row][col] is None:
            for val in range(1,10):
                all_nums = all_nums_in_arr(square)
                if val not in all_nums:
                    square[row][col] = val
                    if check_completion(square):
                        print('Solved')
                        print(square)
                        return True
                    else:
                        if is_currently_valid(square) is True:
                            if solve_square(square):
                                return True
            break
    square[row][col] = None

square = [[None for i in range(3)] for j in range(3)]
solve_square(square)
print(square)
# arr1 = [[1,2,None], [None,3,None], [None,None,None]]
# print(is_valid(arr1))
# # True    (because no rows, columns, or diagonals are completely filled in) 

# arr2 = [[1,2,None], [None,3,None], [None,None,4]] 
# print(is_valid(arr2))
# # False   (because a diagonal is filled in and it doesn't sum to 15)

# arr3 = [[1,2,None], [None,3,None], [5,6,4]] 
# print(is_valid(arr3))
# # False   (because a diagonal is filled in and it doesn't sum to 15)
#         # (it doesn't matter that the bottom row does sum to 15)

# arr4 = [[None,None,None], [None,3,None], [5,6,4]] 
# print(is_valid(arr4))
# # True   (because there is one row that's filled in and it sums to 15)
