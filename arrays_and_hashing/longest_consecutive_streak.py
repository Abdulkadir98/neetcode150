"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

# Uses sorting
# Time Complexity : O(NlogN)
def longest_consecutive_sequence(nums):
    length = len(nums)

    if length == 0:
        return 0
    
    # Sorts list in-place
    nums.sort()
    current_streak = 1
    longest_streak = 1

    for i in range(1, length):
        if nums[i] == nums[i-1]:
            pass
        elif nums[i] == nums[i-1] + 1:
            current_streak += 1
            longest_streak = max(longest_streak, current_streak)
        else:
            current_streak = 1
    return longest_streak

# Uses Set, the solution appears to be quadratic but the inner loop only runs maximum of O(N) so actual time complexity is
# O(N) + O (N) which O(N)
# Another inutition for whether time complexity is O(n^2) or O(n), please take a close look at the entering of the logic: 
# if(!num_set.contains(num-1)).
# That means, for example, 6,5,4,3,2,1 input, only the value 1 is valid for the loop(all other values have its value - 1 in the set), that is O(n).
# Another corner example, 2, 5, 6, 7, 9, 11. All of these numbers are the "entrance" for the logic but the while loop doesn't run much. That is O(n) as well.
def longest_consecutive_sequence_optimized(nums):
    longest_streak = 0
    num_set = set(nums)

    for num in nums:
        if num-1 not in num_set:
            current_num = num
            current_streak = 1

        while current_num + 1 in num_set:
            current_num += 1
            current_streak += 1
        
        longest_streak = max(longest_streak, current_streak)
    return longest_streak

def main():
    nums = [0,3,7,2,5,8,4,6,0,1]
    print(longest_consecutive_sequence(nums))
    print(longest_consecutive_sequence_optimized(nums))


if __name__ == "__main__":
    main()