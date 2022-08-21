'''

SNAIL SORT

Problem: 
    Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

        array = [[1,2,3],
                [4,5,6],
                [7,8,9]]
        snail(array) #=> [1,2,3,6,9,8,7,4,5]
    
    For better understanding, please follow the numbers of the next array consecutively:

        array = [[1,2,3],
                [8,9,4],
                [7,6,5]]
        snail(array) #=> [1,2,3,4,5,6,7,8,9]

'''

# define output = []; n_batch = 0

# Loop: 
#     -> define ROW & COL length
#     -> output += iterate (COL+1) over the first row (left -> right)
#           -> break Loop if len(output) == len(given_arr.flatten())
#     -> output += iterate (ROW LEN) over the last element of each row (top -> bottom)
#     -> output += reverse iterate (COL LEN) over the last row (right -> left)
#     -> output += reverse iterate (ROW-1) over the first element of each row -1 (bottom -> top)
#     -> n_batch += 1

import numpy as np

def snail(snail_map):
    if snail_map == [[]]:
        return []
    
    array = np.array(snail_map)
    ROW_LENGTH, COL_LENGTH = np.shape(array)

    output = []
    n_batch = 0
    
    while True:
        col_batch_len = COL_LENGTH-1-n_batch
        row_batch_len = ROW_LENGTH-1-n_batch

        # print('left to right')
        for col in range(col_batch_len+1-n_batch): # left to right
            output.append(array[n_batch][col+n_batch])
            # print(array[n_batch][col+n_batch])
        if (len(output) == len(array.flatten())): return output
        
        # print('top to bottom')
        for row in range(row_batch_len-n_batch): # top to bottom
            output.append(array[row+1+n_batch][-1-n_batch])
            # print(array[row+1+n_batch][-1-n_batch])
            
        # print('right to left')
        for col in range(col_batch_len-n_batch, 0, -1): # right to left
            output.append(array[-1-n_batch][col-1+n_batch])
            # print(array[-1-n_batch][col-1+n_batch])
        
        # print('bottom to top')
        for row in range(row_batch_len-n_batch-1, 0, -1): # bottom to top
            output.append(array[row+n_batch][n_batch])
            # print(array[row+n_batch][n_batch])
            
        n_batch += 1



class Test:
    def assert_equals(self, solution, answer):
        result = 'Passed' if solution == answer else 'Failed'
        print(result)

test = Test()

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
expected = [1,2,3,6,9,8,7,4,5]
test.assert_equals(snail(array), expected)


array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
expected = [1,2,3,4,5,6,7,8,9]
test.assert_equals(snail(array), expected)

array = [[]]
expected = []
test.assert_equals(snail(array), expected)


array = [[1]]
expected = [1]
test.assert_equals(snail(array), expected)


array = [[1, 2],
         [3, 4],
         [5, 6]]
expected = [1, 2, 4, 6, 5, 3]
test.assert_equals(snail(array), expected)


array = [[1, 2, 3, 4, 5],
         [6, 7, 8, 9, 10],
         [11, 12, 13, 14, 15],
         [16, 17, 18, 19, 20],
         [21, 22, 23, 24, 25]]
expected = [1, 2, 3, 4, 5, 10, 15, 20, 25, 24, 23, 22, 21, 16, 11, 6, 7, 8, 9, 14, 19, 18, 17, 12, 13]
test.assert_equals(snail(array), expected)