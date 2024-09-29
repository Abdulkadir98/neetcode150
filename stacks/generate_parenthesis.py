import collections
"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
"""

# Using Brute Force approach. Generate all combinations of strings of length 2 * N
# Use a queue datastructure for BFS. Start with empty string, dequeue a string and append ")" and "(" to the string
# Check if the string of length 2 * N at every pass and check if it s valid, if yes add it to the answer
# To check if it is valid maintain a count of left parenthesis, if a right parenthesis is encountered decrement 1 else increment 1
# if the count goes below 0 that means there is a right parenthesis for which there is no left parenthesis and so that is not a valid
# string
def generate_parenthesis(n):
    def isValid(p_str):
        left_count = 0
        for p in p_str:
            if p == "(":
                left_count += 1
            else:
                left_count -= 1
                if left_count < 0:
                    return False
        return left_count == 0
    
    answer = []
    queue = collections.deque([""])

    while queue:
        curr_str = queue.popleft()

        if len(curr_str) == 2 * n:
            if isValid(curr_str):
                answer.append(curr_str)
            continue
        queue.append(curr_str + "(")
        queue.append(curr_str + ")")
    return answer

def main():
    answer = generate_parenthesis(3)
    print(answer)

if __name__ == "__main__":
    main()
