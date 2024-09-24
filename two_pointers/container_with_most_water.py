"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""

def maxArea(heights):
    max_area = 0
    left = 0
    right = len(heights) - 1

    while left < right:
        width = right - left
        max_area = max(max_area, min(heights[left], heights[right]) * width)

        # The area is constrained by the shorter line
        # Move the pointer from the shorter line to the other side by one step, the argument is that even
        # though the width is reducing the next line could be taller making up for the reduction in width
        if heights[left] <= heights[right]:
            left += 1
        else:
            right -= 1
    return max_area

def main():
    heights = [1,8,6,2,5,4,8,3,7]
    print(maxArea(heights))

if __name__ == "__main__":
    main()