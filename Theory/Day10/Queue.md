You can directly save this into your `Queue.md`.

# Queue Pattern Notes

## 1. Queue Basics

### Definition

A Queue follows:

```text
FIFO
First In First Out
```

Example:

```python
Queue = [10,20,30]

dequeue()
```

Output:

```python
10
```

The first inserted element is removed first.

---

## Queue Operations

### Enqueue

Add element at rear.

```python
queue.append(10)
```

### Dequeue

Remove element from front.

```python
queue.pop(0)
```

### Peek

Return front element without removing.

### isEmpty

Check whether queue is empty.

---

# Queue vs Stack

| Stack             | Queue              |
| ----------------- | ------------------ |
| LIFO              | FIFO               |
| Last In First Out | First In First Out |
| append()          | append()           |
| pop()             | popleft()          |

Example:

Stack:

```python
[10,20,30]

pop()
```

Output:

```python
30
```

Queue:

```python
[10,20,30]

dequeue()
```

Output:

```python
10
```

---

# 2. Queue Using List

Implementation:

```python
queue = []

queue.append(10)
queue.append(20)

queue.pop(0)
```

Problem:

```python
pop(0)
```

Time Complexity:

```text
O(n)
```

Reason:

Elements shift left after deletion.

Example:

```python
[10,20,30]

pop(0)

[20,30]
```

All elements are shifted.

---

# 3. Queue Using deque

### What is deque?

```text
deque = Double Ended Queue
```

Import:

```python
from collections import deque
```

---

## Operations

### Enqueue

```python
q.append(10)
```

### Dequeue

```python
q.popleft()
```

### Peek

```python
q[0]
```

### Empty Check

```python
len(q) == 0
```

---

## Example

```python
from collections import deque

q = deque()

q.append(10)
q.append(20)
q.append(30)

print(q.popleft())
```

Output:

```python
10
```

---

## Complexity

| Operation | Complexity |
| --------- | ---------- |
| append()  | O(1)       |
| popleft() | O(1)       |
| peek      | O(1)       |

---

## Interview Question

Why use deque instead of list?

Answer:

```text
List pop(0) takes O(n) because elements shift.

deque.popleft() takes O(1).
```

---

# 4. Queue Using Two Stacks

## Problem

Implement Queue using:

```python
stack1
stack2
```

---

## Core Idea

### Enqueue

Always push into stack1.

```python
stack1.append(x)
```

---

### Dequeue

If stack2 is empty:

Move all elements from stack1 to stack2.

```python
while stack1:
    stack2.append(stack1.pop())
```

Then:

```python
stack2.pop()
```

---

## Why Transfer?

Example:

```python
stack1 = [10,20,30]
```

Transfer:

```python
stack2 = [30,20,10]
```

Now:

```python
stack2.pop()
```

returns:

```python
10
```

which is the front of the queue.

---

## Peek

```python
stack2[-1]
```

returns front element.

---

## Complexity

| Operation | Complexity     |
| --------- | -------------- |
| enqueue   | O(1)           |
| dequeue   | O(1) amortized |
| peek      | O(1) amortized |

Space:

```text
O(n)
```

---

# 5. Sliding Window + Queue

## Problem

Number of Recent Calls

LeetCode 933

---

### Input

```python
ping(1)
ping(100)
ping(3001)
ping(3002)
```

Output:

```python
1
2
3
3
```

---

## Pattern

```text
Sliding Window + Queue
```

---

## Observation

Keep only requests in:

```python
[t-3000, t]
```

Remove older requests.

---

## Solution

```python
from collections import deque

class RecentCounter:

    def __init__(self):
        self.q = deque()

    def ping(self, t):

        self.q.append(t)

        while self.q[0] < t - 3000:
            self.q.popleft()

        return len(self.q)
```

---

## Why Queue?

Oldest requests expire first.

Example:

```python
1
100
3001
3002
```

Request:

```python
1
```

becomes invalid first.

FIFO → Queue.

---

## Complexity

Time:

```text
O(1) amortized
```

Space:

```text
O(n)
```

---

# Queue Patterns Learned

### Pattern 1

```text
Basic Queue
```

Examples:

* Ticket System
* Printer Queue

---

### Pattern 2

```text
Queue using deque
```

Examples:

* BFS
* Sliding Window

---

### Pattern 3

```text
Queue using Two Stacks
```

Interview Favorite.

---

### Pattern 4

```text
Sliding Window + Queue
```

Examples:

* RecentCounter
* Streaming Data Problems

---

# Interview Cheat Sheet

Queue:

```text
FIFO
```

Best Python Implementation:

```python
from collections import deque
```

Front:

```python
q[0]
```

Insert:

```python
q.append(x)
```

Remove:

```python
q.popleft()
```

Complexities:

```text
append()   -> O(1)
popleft()  -> O(1)
peek()     -> O(1)
```

Tomorrow, the natural next step after Queue is **BFS (Breadth First Search)** because BFS is essentially a queue application and is asked much more frequently than advanced queue questions.
