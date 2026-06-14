Perfect. Before code, let's understand **what Clone Graph is actually asking**, because most people get confused by the word "Graph".

---

# What is a Graph?

Think of it like friends connected to each other.

Example:

```text
1 ----- 2
|       |
|       |
4 ----- 3
```

Connections:

```text
1 → 2,4

2 → 1,3

3 → 2,4

4 → 1,3
```

---

# What does "Clone Graph" mean?

Suppose someone gives you:

```text
Original Graph
```

You need to create:

```text
New Graph
```

with:

* New nodes
* Same values
* Same connections

---

Example:

Original

```text
1 ----- 2
|       |
|       |
4 ----- 3
```

Clone

```text
1' ----- 2'
|         |
|         |
4' ----- 3'
```

Notice:

```text
1' is NOT 1

2' is NOT 2
```

They are completely new nodes.

---

# Why can't we just copy values?

Suppose:

```text
1 → [2,4]
```

If we only copy:

```python
Node(1)
```

then:

```text
Connections are lost
```

We must copy:

```text
Node
+
Neighbors
```

---

# Graph Node Structure

LeetCode gives:

```python
class Node:

    def __init__(self,val=0,neighbors=None):

        self.val = val
        self.neighbors = neighbors if neighbors else []
```

Example:

```python
node1 = Node(1)
node2 = Node(2)

node1.neighbors.append(node2)
```

Means:

```text
1 ----> 2
```

---

# Biggest Problem

Look at graph:

```text
1 ----- 2
|       |
|       |
4 ----- 3
```

If we do BFS:

```text
1
↓
2
↓
3
↓
4
↓
1 again
```

Infinite loop.

---

# Solution

We need:

```text
Visited Dictionary
```

---

# Why Dictionary?

We need to remember:

```text
Original Node
      ↓
Cloned Node
```

Example:

```python
visited = {

node1 : clone1,

node2 : clone2,

node3 : clone3

}
```

---

# Visual

Original:

```text
1
```

Create:

```text
1'
```

Store:

```python
visited[node1] = clone1
```

Now whenever we see:

```text
node1
```

again,

we don't create another copy.

---

# BFS Approach

Start:

```text
queue = [node1]
```

Create clone:

```python
clone1 = Node(1)
```

Store:

```python
visited[node1] = clone1
```

---

Process node1

Neighbors:

```text
2
4
```

---

Create clones:

```python
clone2 = Node(2)
clone4 = Node(4)
```

Store:

```python
visited[node2] = clone2

visited[node4] = clone4
```

---

Connect them:

```python
clone1.neighbors.append(clone2)

clone1.neighbors.append(clone4)
```

---

Queue becomes:

```python
[2,4]
```

---

Process 2

Neighbor:

```text
1
```

Already exists?

```python
node1 in visited
```

YES

Don't create again.

Just connect:

```python
clone2.neighbors.append(clone1)
```

---

# Pattern Recognition

Whenever you see:

```text
Graph

Nodes

Connections

Neighbors

Clone

Copy Graph
```

Think:

```text
BFS
Queue
Visited Dictionary
```

---

# Why HashMap / Dictionary?

Not for visited only.

It stores:

```text
Original Node
        ↓
Copied Node
```

This is the key idea.

---

# Dry Run Question

Suppose:

```text
1 ---- 2
```

We start from:

```text
node1
```

We create:

```python
visited = {
    node1 : clone1
}
```

Now while processing node1, we see neighbor:

```text
node2
```

Question:

Should we:

### A)

Create a new clone for node2

OR

### B)

Use visited[node2]

Which one and why?

This is the most important concept before we write the code.






Clone Graph

Input:
Node object

Pattern:
BFS + Queue + HashMap

Queue:
Stores original nodes

Visited Dictionary:
original_node -> cloned_node

Why dictionary?
Need mapping between original and cloned nodes.

Time: O(V + E)

Space: O(V)


