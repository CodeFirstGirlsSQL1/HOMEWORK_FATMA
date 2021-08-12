"""
SEARCH IN MATRIX
--------

You are given a matrix (a list of lists) of DISTINCT integers and a target number.
Each row in the matrix is SORTED and each column in the matrix is SORTED.
Our matrix does not necessarily have the same height and width.

Write a function that returns a list of the row and column indices of the target integer
IF it is contained in the matrix, otherwise return [-1, -1].

EXAMPLE INPUT

matrix = [
[1,4,7,12,15,1000],
[2,5,19,31,32,1001],
[3,8,24,33,35,1002],
[40,41,42,44,45,1003],
[99,100,103,106,128,1004]
]

target =44

EXAMPLE OUTPUT

result = [3,3]

"""

"""
First attempt using a for loop and a check to see if the target is in the list
then use .index() to get the index number of it, in order to not use a second 
for loop

"""
def search_in_matrix(matrix, target):
    row, col = [-1, -1]
    found = False

    for rows in matrix:
        # increment the row value as we loop through the matrix rows
        row += 1
        if target in rows:
            # if the target is in the list
            # then set the col as its index
            col = rows.index(target)
            found = True
            break;

    return [row, col] if found else [-1, -1]
    
matrix = [
[1,4,7,12,15,1000],
[2,5,19,31,32,1001],
[3,8,24,33,35,1002],
[40,41,42,44,45,1003],
[99,100,103,106,128,1004]
]

print(search_in_matrix(matrix, 4)) # returns [0, 1]


"""
second attempt at the question in trying not to rely on and use the
in keyword or the index() method. 
this time I use a while loop and check the matrix from top right
as wach list is sorted and each column value increases as i travel down the 
matrix
"""

def search_in_matrix(matrix, target):
    col, row = [0, 0]
    col = len(matrix[row]) - 1
    
    while (row != (len(matrix) - 1)):
        if target < matrix[row][col]:
            # check the number before in that row
            col -= 1
            
        if target > matrix[row][col]:
            # go down to the next row and 
            # start from the back of the list again
            row += 1
            col = len(matrix[row]) - 1
            
        if target == matrix[row][col]:
            return [row, col]
            
    return [-1, -1]
    
matrix = [
[1,4,7,12,15,1000],
[2,5,19,31,32,1001],
[3,8,24,33,35,1002],
[40,41,42,44,45,1003],
[99,100,103,106,128,1004]
]

print(search_in_matrix(matrix, 44)) # returns [3, 3]









