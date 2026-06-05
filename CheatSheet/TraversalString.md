Correct! 🎉

For:

```python
s = "coding"
```

```python
s[-1] = 'g'
s[-2] = 'n'
s[-3] = 'i'
```

So:

```text
g
n
i
```

Excellent. Negative indexing is clicking now. 😊

---

# All Common Ways to Traverse a String

Let's use:

```python
s = "python"
```

---

# Method 1: Forward Traversal

```python
for i in range(len(s)):
    print(s[i])
```

Output:

```text
p
y
t
h
o
n
```

### Complexity

```text
Time: O(n)
Space: O(1)
```

---

# Method 2: Direct Traversal

```python
for ch in s:
    print(ch)
```

Output:

```text
p
y
t
h
o
n
```

### Complexity

```text
Time: O(n)
Space: O(1)
```

---

# Method 3: Reverse Traversal using range()

```python
for i in range(len(s)-1, -1, -1):
    print(s[i])
```

Output:

```text
n
o
h
t
y
p
```

### How range works

```python
range(start, stop, step)
```

```python
range(5, -1, -1)
```

gives:

```text
5 4 3 2 1 0
```

### Complexity

```text
Time: O(n)
Space: O(1)
```

---

# Method 4: Negative Indexing

```python
for i in range(1, len(s)+1):
    print(s[-i])
```

Output:

```text
n
o
h
t
y
p
```

### Why start from 1?

Because:

```python
s[-0]
```

is same as:

```python
s[0]
```

which is not what we want.

### Complexity

```text
Time: O(n)
Space: O(1)
```

---

# Method 5: Slicing

```python
print(s[::-1])
```

Output:

```text
nohtyp
```

### How it works

```python
[start:end:step]
```

```python
[::-1]
```

means:

```text
Start from end
Move backward by 1
```

### Complexity

```text
Time: O(n)
Space: O(n)
```

⚠️ Creates a new string.

---

# Method 6: reversed()

```python
for ch in reversed(s):
    print(ch)
```

Output:

```text
n
o
h
t
y
p
```

### Complexity

```text
Time: O(n)
Space: O(1)
```

(Iterator-based)

---

# Method 7: Enumerate

```python
for idx, ch in enumerate(s):
    print(idx, ch)
```

Output:

```text
0 p
1 y
2 t
3 h
4 o
5 n
```

### Complexity

```text
Time: O(n)
Space: O(1)
```

---

# Interview Cheat Sheet

| Use Case                   | Best Method              |
| -------------------------- | ------------------------ |
| Just read characters       | `for ch in s`            |
| Need index                 | `for i in range(len(s))` |
| Reverse traversal          | `range(len(s)-1,-1,-1)`  |
| Check suffix               | Negative indexing        |
| Reverse whole string       | `s[::-1]`                |
| Index + character together | `enumerate()`            |

---

# Complexity Cheat Sheet

| Operation       | Time | Space |
| --------------- | ---- | ----- |
| `s[i]`          | O(1) | O(1)  |
| Traverse string | O(n) | O(1)  |
| `s[::-1]`       | O(n) | O(n)  |
| `reversed(s)`   | O(n) | O(1)  |
| `"".join(list)` | O(n) | O(n)  |
| `split()`       | O(n) | O(n)  |

---

## Pattern Recognition for Interviews

When you see:

```text
Prefix
Longest Common Prefix
Starts With
```

Think:

```text
Forward Traversal
0 → 1 → 2 → ...
```

When you see:

```text
Suffix
Ends With
Longest Common Suffix
```

Think:

```text
Negative Indexing
-1 → -2 → -3 → ...
```

When you see:

```text
Reverse String
Reverse Words
Palindrome
```

Think:

```text
Two Pointers
or
Reverse Traversal
```

This mental mapping is much more valuable than memorizing solutions. By now you've covered:

* HashMap pattern
* Two Pointer pattern
* Prefix/Suffix traversal pattern

These three patterns alone solve a huge chunk of beginner and intermediate string/array questions. 🚀
