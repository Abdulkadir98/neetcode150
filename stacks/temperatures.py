"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
"""

# Solved using a monotonic stack (elements are in sorted order, decreasing in this case)
# We store the index of the temperature in the stack, since we care about the difference of indices
# If the stack is empty or if the temperature is less than the temperature of the day at the top of the stack 
# we simply push the current day (current index) to the stack and move on
# If we see a temperature that is warmer: we pop the stack and set the ans of the previous day to current day - previous day
# we keep popping until the top of the stack is not colder than the current day
# Time complexity: O(N)
# It may seem it is O(N^2) due to the nested loop but every element gets pushed/popped onto the stack only once. So the stack operations
# is limited to the length of the temperatures list (N)
def main(temperatures):
    ans = [0] * len(temperatures)
    stack = []

    for curr_day, curr_temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < curr_temp:
            prev_day = stack.pop()
            ans[prev_day] = curr_day - prev_day
        stack.append(curr_day)
    
    return ans

if __name__ == "__main__":
    temperatures = [73,74,75,71,69,72,76,73]
    ans = main(temperatures=temperatures)
    print(ans)