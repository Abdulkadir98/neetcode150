"""
Given two strings s1 and s2, return true if s2 contains a 
permutation
 of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
"""

from collections import Counter, defaultdict

def checkInclusion(t, s):

    need = Counter(t)
    window = defaultdict(int)

    left, right = 0, 0
    valid = 0

    while right < len(s):
        c = s[right]
        right += 1

        if c in need:
            window[c] += 1
            if window[c] == need[c]:
                valid += 1
        
        while (right - left >= len(t)):
            if valid == len(need):
                return True
            
            d = s[left]
            left += 1
            if d in need:
                if window[d] == need[d]:
                    valid -= 1
                window[d] -= 1
    
    return False

def main():
    s = "eidbaooo"
    t = "ab"

    print(f'Does {s} contain a permutation of {t}?: {checkInclusion(t, s)}')

if __name__ == "__main__":
    main()
        
            
                
