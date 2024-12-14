"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
"""

def search(matrix, target):
    m = len(matrix)
    if m == 0:
        return False
    
    n = len(matrix[0])

    # Consider the 2d matrix to be a 1d array and do standard binary search
    # row_idx = mid // number of columns
    # col_idx = mid % number of columns
    left,right = 0, m*n - 1
    while left <= right:
        mid = (left + right) // 2
        row_idx = mid // n
        col_idx = mid % n
        num = matrix[row_idx][col_idx]

        if num == target:
            return True
        elif num > target:
            right = mid - 1
        else:
            left = mid + 1
    
    return False

def main():
    input = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3

    print(search(input, target))

if __name__ == "__main__":
    main()