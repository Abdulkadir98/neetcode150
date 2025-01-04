"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
 

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104
"""

"""
Algorithm Intuition:
1. If the array is rotated then there is a pivot index which divides the array into two halves. The array to the left of the pivot index is sorted
And array to the right (including the pivot index is sorted). Therefore we find the pivot index first which is nothing but the minimum value of the array
2. After finding the pivot index we have the boundary values needed to perform binary search- We search in the array to left of the pivot index, if we find target we return
the index. If not we search to the right
"""
def search(nums, target):

    pivot_idx = find_pivot_index(nums)
    print(f'Pivot idx is {pivot_idx}')
    res = binary_search(nums, target, 0, pivot_idx-1)

    if res == -1:
        res = binary_search(nums, target, pivot_idx, len(nums)-1)

    return res


def binary_search(nums, target, left, right):
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1



def find_pivot_index(nums):
    n = len(nums)
    if n == 1 or nums[0] < nums[n-1]:
        return 0
    
    left, right = 0, n-1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > nums[-1]:
            left = mid + 1
        else:
            right = mid - 1
    
    return left

def main():
    nums = [4,5,6,7,0,1,2]
    print(search(nums, 0))

    nums2 = [4,5,6,7,0,1,2]
    print(search(nums2, 3))

    nums3 = [1]
    print(search(nums3, 0))

if __name__ == "__main__":
    main()