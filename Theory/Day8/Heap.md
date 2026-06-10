Good idea. Don't jump into `heapq` until the concept is clear.

# What is a Heap?

A **Heap** is a special tree-based data structure used to efficiently find:

* Smallest element
* Largest element
* Top K elements

without sorting the entire array.

---

# Real-Life Analogy

Imagine a hospital emergency queue.

Patients:

```text
Anisha  -> Priority 1 (Critical)
Rahul   -> Priority 3
Amit    -> Priority 2
```

Who should be served first?

```text
Anisha
```

because she has the highest priority.

A Heap helps us efficiently maintain this priority order.

---

# Types of Heap

## 1. Min Heap

Smallest element is always on top.

Example:

```text
        1
      /   \
     3     5
    / \
   7   8
```

Top element:

```text
1
```

---

## 2. Max Heap

Largest element is always on top.

Example:

```text
        10
       /  \
      8    7
     / \
    3   2
```

Top element:

```text
10
```

---

# Why Not Sort?

Suppose:

```python
nums = [5,2,9,1,7]
```

Need largest element.

### Sorting

```python
sorted(nums)
```

Complexity:

```text
O(n log n)
```

---

### Heap

Largest/smallest available immediately at top.

Complexity:

```text
O(log n)
```

for insert/remove.

Much faster when data keeps changing.

---

# Heap Property

A Heap is NOT fully sorted.

Many beginners think:

```text
Heap = Sorted Array
```

❌ Wrong

Example Min Heap:

```python
[1,3,2,7,5]
```

This is a valid heap.

Notice:

```python
3 > 2
```

yet it's still valid.

Why?

Because only the parent-child relationship matters.

---

# Min Heap Rule

Every parent must be smaller than its children.

Example:

```text
        1
      /   \
     3     2
    / \
   7   5
```

Valid Min Heap.

---

# Max Heap Rule

Every parent must be larger than its children.

Example:

```text
        10
       /  \
      8    7
     / \
    3   2
```

Valid Max Heap.

---

# Why Interviewers Love Heaps

When you hear:

```text
Top K Frequent Elements
K Largest Element
K Smallest Element
Merge K Sorted Lists
Priority Scheduling
Median From Data Stream
```

Immediately think:

```text
Heap
```

---

# Python's heapq

Python gives:

```python
import heapq
```

Important:

```text
heapq = Min Heap
```

by default.

---

# Basic Operations

## Create Heap

```python
import heapq

nums = [4,1,3]

heapq.heapify(nums)

print(nums)
```

Result:

```python
[1,4,3]
```

Smallest element moves to top.

---

## Insert

```python
heapq.heappush(nums, 2)
```

---

## Remove Smallest

```python
heapq.heappop(nums)
```

Returns:

```python
1
```

---

# Complexity Cheat Sheet

| Operation     | Complexity |
| ------------- | ---------- |
| heapify       | O(n)       |
| heappush      | O(log n)   |
| heappop       | O(log n)   |
| peek smallest | O(1)       |

---

# Why Heaps Matter for Top K

Suppose:

```python
nums = [1,1,1,2,2,3,4,4,4,4]
k = 2
```

Frequencies:

```python
{
1:3,
2:2,
3:1,
4:4
}
```

We only need:

```text
Top 2
```

not all elements sorted.

A heap lets us keep only the best K candidates instead of sorting everything.

---

### Interview Cheat Sheet

| Question Type        | Pattern |
| -------------------- | ------- |
| Top K Frequent       | Heap    |
| K Largest            | Heap    |
| K Smallest           | Heap    |
| Priority Queue       | Heap    |
| Running Median       | Heap    |
| Merge K Sorted Lists | Heap    |

Before we touch code, tell me:

For **Top K Frequent Elements**, do you think we need a **Min Heap** or a **Max Heap**? And why? That's the key intuition interviewers often probe before asking for the implementation.
