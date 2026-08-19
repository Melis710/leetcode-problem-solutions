class MinStack:
    # Maintains two stack: 
    # * primary abstracted (internal) data structure stack  
    # * auxiliary stack maintaining minimum value

    # time complexity: O(1) for push, pop, top and getMin
    # space complexity: O(n) with an optimization to use less space 
    # by only storing values when the minimum updates

    def __init__(self):
        self.stack = []  # primary data structure
        self.min_stack = []  # auxiliary stack maintaining minimum value 

    def push(self, value: int) -> None:
        self.stack.append(value)  # always append the value to the primary stack
        # if min_stack is empty, initialize it or if the value is a new min, push it
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self) -> None:
        if self.stack.pop() == self.getMin():  # synchronize min_stack in case the popped value was the min
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]  # return the last element

    def getMin(self) -> int:
        return self.min_stack[-1]  # return the up-to-date minimum


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()