"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
"""
"""
Intuition: If the array is rotated then there is a point in the array where the number decreases and then starts increasing again, that boundary is the minimum
If the array is not rotated then the first element is the minimum since the array is sorted.
We can use binary search algorithm:
1) After finding mid we check if mid is greater than the last element if yes, that means the array is rotated and we search to the right of the mid
2) Otherwise we search to the left of the mid

"""
def search(nums):
    left = 0
    right = len(nums) - 1

    if len(nums) == 1 or nums[left] < nums[right]:
        return nums[left]
    
    while left <= right:
        mid = (left + right) // 2

        if nums[mid] > nums[-1]:
            left = mid + 1
        else:
            right = mid - 1
    return nums[left]

def main():
    nums = [4, 5, 6, 7, 0, 1, 2]
    print(search(nums))

if __name__ == "__main__":
    main()