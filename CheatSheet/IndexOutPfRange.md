This is one of the most common problems beginners face. The good news is that **90% of "Index Out of Range" errors come from just a few patterns.**

---

# Rule 1: When using `i+1`

❌ Dangerous:

```python
for i in range(len(arr)):
    print(arr[i+1])
```

Last iteration:

```python
i = len(arr)-1
```

Then:

```python
arr[len(arr)]
```

❌ Out of range.

---

✅ Fix:

```python
for i in range(len(arr)-1):
    print(arr[i+1])
```

### Example

```python
arr=[1,2,3,4]
```

Valid indices:

```text
0 1 2 3
```

If using:

```python
arr[i+1]
```

Maximum i can be:

```python
2
```

because:

```python
arr[3]
```

is the last valid index.

---

# Rule 2: When using `i-1`

❌

```python
for i in range(len(arr)):
    arr[i-1]
```

Python won't crash because:

```python
arr[-1]
```

means last element.

But logically it may be wrong.

---

✅ Fix

```python
for i in range(1,len(arr)):
```

Now:

```python
arr[i-1]
```

is always safe.

---

# Rule 3: Two Pointers

Always check:

```python
while i < j:
```

not

```python
while i <= j:
```

unless you really need middle element.

Example:

```python
arr=[1]
```

```python
i=0
j=0
```

---

# Rule 4: Sliding Window

Most common mistake:

```python
for i in range(k,len(arr)):
    cur_sum = cur_sum-arr[j]+arr[i]
```

Forgetting:

```python
j+=1
```

Then window boundaries break.

---

# Rule 5: Stack Top

❌

```python
stack[-1]
```

when stack is empty.

---

Always write:

```python
if stack:
    stack[-1]
```

or

```python
while stack and ...
```

Like you already do:

```python
while stack and nums[stack[-1]]<=nums[i]:
```

✅ Safe

---

# Rule 6: String Access

If using:

```python
s[i+1]
```

then:

```python
for i in range(len(s)-1)
```

---

# Rule 7: Nested Loop Comparison

For sorted check:

❌

```python
for i in range(len(arr)):
    arr[i+1]
```

---

✅

```python
for i in range(len(arr)-1):
```

---

# My Personal Interview Checklist

Whenever I write:

### `i+1`

Immediately ask:

```text
Can i reach last index?
```

If yes:

```python
range(len(arr)-1)
```

---

### `i-1`

Ask:

```text
Can i become 0?
```

If yes:

```python
range(1,len(arr))
```

---

### `stack[-1]`

Ask:

```text
Can stack be empty?
```

If yes:

```python
if stack:
```

---

### `arr[j]`

Ask:

```text
Can j become len(arr)?
```

If yes:

Need boundary check.

---

# Quick Formula Sheet

| Accessing  | Safe Range       |
| ---------- | ---------------- |
| `arr[i]`   | `0 → len(arr)-1` |
| `arr[i+1]` | `0 → len(arr)-2` |
| `arr[i-1]` | `1 → len(arr)-1` |
| `arr[j+1]` | `j < len(arr)-1` |
| `arr[j-1]` | `j > 0`          |

---

# What I Recommend For You

Before running any code, look at every index expression:

```python
arr[i]
arr[i+1]
arr[i-1]
arr[j]
arr[j+1]
stack[-1]
```

and ask:

> What is the maximum possible value of i/j here?

After about 20-30 problems, you'll automatically spot index issues before running the code.

From the solutions you've shown so far, your most common mistakes are:

1. Using `range(len(arr))` when accessing `i+1`
2. Forgetting stack empty checks
3. Off-by-one errors in suffix/prefix problems

These are completely normal and improve quickly with practice.
