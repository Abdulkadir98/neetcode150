"""
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""
from collections import Counter

def lengthOfLongestSubstring(s):

    chars = Counter()
    left = right = 0
    res = 0

    while right < len(s):
        r = s[right]
        chars[r] += 1

        while chars[r] > 1:
            l = s[left]
            chars[l] -= 1
            left += 1
        
        res = max(res, right - left + 1)
        right += 1
    
    return res

def main():
    s = "abcabcbb"

    print(f'Length of the longest substring without repeating chars: {lengthOfLongestSubstring(s)}')

if __name__ == "__main__":
    main()
