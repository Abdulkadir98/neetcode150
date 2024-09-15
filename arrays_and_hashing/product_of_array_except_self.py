"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)"""


def prod_of_array(nums):
    length = len(nums)

    L, R, answer = [0] * length, [0] * length, [0] * length
    L[0] = 1
    R[length - 1] = 1

    for i in range(1, length):
        L[i] = L[i-1] * nums[i-1]

    for i in reversed(range(length - 1)):
        R[i] = R[i+1] * nums[i+1]

    for i in range(length):
        answer[i] = L[i] * R[i]

    return answer

# 1. Instead of constructing two separate arrays L, R we the same answer array
# 2. We track running product of l_prod and r_prod and add it to the answer array
def prod_of_array_space_optimized(nums):
    length = len(nums)
    l_prod = 1
    r_prod = 1
    answer = [0] * length

    for i in range(length):
        answer[i] = l_prod
        l_prod *= nums[i]

    for i in range(length-1, -1, -1):
        answer[i] *= r_prod
        r_prod *= nums[i]

    return answer


def main():
    nums = [1, 2, 3, 4]
    print(prod_of_array(nums))
    print(prod_of_array_space_optimized(nums))



if __name__ == "__main__":
    main()
