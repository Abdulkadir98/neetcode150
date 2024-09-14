"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
"""

# Using Quick Select Algorithm
# Average case time complexity is O(N)

from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        unique = list(count.keys())

        def partition(left, right, pivot_index):
            pivot_frequency = count[unique[pivot_index]]

            # Move pivot to the end
            unique[pivot_index], unique[right] = unique[right], unique[pivot_index]

            store_index = left

            # Move all left frequent elements to the left
            for i in range(left, right):
                if count[unique[i]] < pivot_frequency:
                    unique[store_index], unique[i] = unique[i], unique[store_index]
                    store_index += 1

            # Move to the pivot to its final place
            unique[right], unique[store_index] = unique[store_index], unique[right]
            return store_index 

        def quickselect(left, right, k_smallest):
            if left == right:
                return
            
            pivot_index = random.randint(left, right)

            pivot_index = partition(left, right, pivot_index)

            if k_smallest == pivot_index:
                return
            elif k_smallest < pivot_index:
                quickselect(left, pivot_index - 1, k_smallest)
            else:
                quickselect(pivot_index + 1, right, k_smallest)
        
        n = len(unique)
        quickselect(0, n-1, n-k)

        return unique[n-k:]
