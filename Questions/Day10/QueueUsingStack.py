# Approach
# Use two stacks:
# stack1 → used for enqueue
# stack2 → used for dequeue/peek
# Enqueue:
# Directly push into stack1.
# Dequeue:
# If stack2 is empty:
# Move all elements from stack1 to stack2.
# Pop from stack2.
# Peek:
# Same transfer logic as dequeue.
# Return top of stack2.


class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x):
        self.stack1.append(x)

    def dequeue(self):

        if not self.stack2:

            while self.stack1:
                self.stack2.append(self.stack1.pop())

        if not self.stack2:
            return "Queue is Empty"

        return self.stack2.pop()

    def peek(self):

        if not self.stack2:

            while self.stack1:
                self.stack2.append(self.stack1.pop())

        if not self.stack2:
            return "Queue is Empty"

        return self.stack2[-1]

    def empty(self):
        return len(self.stack1) == 0 and len(self.stack2) == 0


q = MyQueue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.stack1)

print(q.peek())      # 10
print(q.dequeue())   # 10
print(q.dequeue())   # 20

q.enqueue(40)

print(q.peek())      # 30
print(q.dequeue())   # 30
print(q.dequeue())   # 40

print(q.empty())     # True


# | Operation | Complexity     |
# | --------- | -------------- |
# | enqueue   | O(1)           |
# | dequeue   | O(1) amortized |
# | peek      | O(1) amortized |
# | empty     | O(1)           |
#This optimization gives an amortized O(1) dequeue operation.