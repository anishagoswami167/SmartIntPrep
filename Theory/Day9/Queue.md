Perfect. Let's do the second DSA question for Day 9.

# Queue Using List

## What is a Queue?

Queue follows:

```text
FIFO
First In First Out
```

Example:

```text
10 → 20 → 30
```

If we remove an element:

```text
10 leaves first
```

because it entered first.

---

# Queue Operations

## Enqueue (Insert)

Add element at the rear.

```python
queue.append(x)
```

Example:

```python
queue = []

queue.append(10)
queue.append(20)

print(queue)
```

Output:

```python
[10,20]
```

---

## Dequeue (Remove)

Remove element from front.

```python
queue.pop(0)
```

Example:

```python
queue = [10,20]

queue.pop(0)
```

Output:

```python
10
```

Remaining:

```python
[20]
```

---

## Peek

Look at front element.

```python
queue[0]
```

Example:

```python
queue = [10,20,30]

print(queue[0])
```

Output:

```python
10
```

---

## isEmpty

```python
len(queue) == 0
```

---

# Dry Run

Initial:

```python
queue = []
```

### enqueue(10)

```python
[10]
```

### enqueue(20)

```python
[10,20]
```

### enqueue(30)

```python
[10,20,30]
```

### dequeue()

Remove first element:

```python
10
```

Queue becomes:

```python
[20,30]
```

### peek()

```python
20
```

---

# Your Task

Write a Queue class with:

```python
enqueue(x)
dequeue()
peek()
isEmpty()
```

Skeleton:

```python
class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, x):
        pass

    def dequeue(self):
        pass

    def peek(self):
        pass

    def isEmpty(self):
        pass
```

Try writing it yourself first.

---

### Interview Question

After you write it, I'll ask:

> Why is `pop(0)` inefficient in Python lists?

That's a very common follow-up.

class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, x):
        self.queue.append(x)

    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        return self.queue.pop(0)

    def peek(self):
        if self.isEmpty():
            return "Queue is Empty"
        return self.queue[0]

    def isEmpty(self):
        return len(self.queue) == 0

q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.dequeue()
q.peek()
q.isEmpty()


Time Complexity
enqueue()
queue.append(x)

Time:

O(1)
peek()
queue[0]

Time:

O(1)
isEmpty()
len(queue)==0

Time:

O(1)
dequeue()
queue.pop(0)

Time:

O(n)

⚠️ This is the famous interview follow-up.

Why?

Suppose:

[10,20,30,40]

Remove:

10

Python must shift:

20 -> index 0
30 -> index 1
40 -> index 2

All elements move one position.

Therefore:

O(n)
Interview Follow-Up

Because pop(0) is O(n), Python interviews often ask:

What's a better data structure for implementing Queue?

Answer:

from collections import deque

where: popleft() is: O(1)

We'll cover deque when we do the next Queue/Sliding Window topics. For now, you've completed Day 9's Queue fundamentals. ✅