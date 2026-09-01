# Problem Statement

# Design a stack that supports the following operations:

# push(x)
# pop()
# top()
# getMin()

# All operations should run in:

# O(1)


class MinStack:

    def __init__(self):

        self.stack = []
        self.minStack = []

    def push(self, val):

        self.stack.append(val)

        if not self.minStack:
            self.minStack.append(val)

        else:

            current_min = min(
                val,
                self.minStack[-1]
            )

            self.minStack.append(current_min)

    def pop(self):

        self.stack.pop()
        self.minStack.pop()

    def top(self):

        return self.stack[-1]

    def getMin(self):

        return self.minStack[-1]


obj = MinStack()

obj.push(7)
obj.push(3)
obj.push(5)
obj.push(2)

print("Minimum:", obj.getMin())

obj.pop()

print("Minimum after pop:", obj.getMin())

print("Top:", obj.top())

# Output

# Minimum: 2

# Minimum after pop: 3

# Top: 5

# Min Stack uses two stacks:
# one stores values and the other stores the minimum value seen so far at every position, allowing getMin() in O(1) time.