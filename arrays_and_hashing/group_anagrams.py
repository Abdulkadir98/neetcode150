"""
Given an array of strings strs, group the 
anagrams
 together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""

def main():
    strs = ["eat","tea","tan","ate","nat","bat"]
    out = groupAnagrams(strs)
    print(out)

def groupAnagrams(strs):
    res = []
    if len(strs) == 1:
        res.append(strs)
        return res
    
    anagram_map = {}
    for a_str in strs:
        sorted_str = ''.join(sorted(a_str))
        if sorted_str not in anagram_map:
            anagram_map[sorted_str] = [a_str]
        elif sorted_str in anagram_map:
            anagram_group = anagram_map[sorted_str]
            anagram_group.append(a_str)
            anagram_map[sorted_str] = anagram_group
    for group in anagram_map.values():
        res.append(group)

    return res

if __name__ == "__main__":
    main()