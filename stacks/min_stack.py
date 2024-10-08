"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
 

Constraints:

-231 <= val <= 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.
"""

# Maintaining the current min value for every value of the stack
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val):
        if not self.stack:
            self.stack.append((val, val))
            return
        current_min = self.stack[-1][1]
        self.stack.append((val, min(current_min, val)))
    
    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1][0]
    
    def getMin(self):
        return self.stack[-1][1]
    
def main():
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin()) # return -3
    minStack.pop()
    minStack.top()    # return 0
    print(minStack.getMin()) # return -2

if __name__ == "__main__":
    main()
