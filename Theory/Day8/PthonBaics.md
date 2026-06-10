# Day 8 Python Basics - Dictionaries & Sets Deep Dive

## 1. Dictionary Frequency Count

### Problem

Count the frequency of each element.

### Example

```python
nums = [1,2,2,3,3,3]

freq = {}

for n in nums:
    freq[n] = freq.get(n, 0) + 1

print(freq)
```

### Output

```python
{1:1, 2:2, 3:3}
```

### Explanation

`get(key, default)` returns the value of the key if present, otherwise returns the default value.

Example:

```python
d = {}

print(d.get('a', 0))
```

Output:

```python
0
```

### Time Complexity

```text
O(n)
```

### Space Complexity

```text
O(n)
```

---

## 2. First Non-Repeating Character

### Problem

Find the first character that appears only once.

### Example

```python
s = "eettcodelc"
```

### Output

```python
o
```

### Solution

```python
def nonRepChar(s):

    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in s:
        if freq[ch] == 1:
            return ch

    return None


print(nonRepChar("eettcodelc"))
```

### Time Complexity

```text
O(n)
```

### Space Complexity

```text
O(n)
```

### Pattern

```text
HashMap / Frequency Count
```

---

## 3. Contains Duplicate

### Problem

Determine if an array contains duplicate elements.

### Example

```python
nums = [1,2,3,1]
```

### Output

```python
True
```

### Solution

```python
def containsDuplicate(nums):

    seen = set()

    for num in nums:

        if num in seen:
            return True

        seen.add(num)

    return False


print(containsDuplicate([1,2,3,1]))
```

### Time Complexity

```text
O(n)
```

### Space Complexity

```text
O(n)
```

### Pattern

```text
HashSet
```

---

# Dictionary Methods

## get()

### Example

```python
d = {'a':1}

print(d.get('a'))
print(d.get('b'))
print(d.get('b',0))
```

### Output

```python
1
None
0
```

---

## keys()

```python
d = {'a':1,'b':2}

print(d.keys())
```

### Output

```python
dict_keys(['a', 'b'])
```

---

## values()

```python
d = {'a':1,'b':2}

print(d.values())
```

### Output

```python
dict_values([1, 2])
```

---

## items()

```python
d = {'a':1,'b':2}

for k, v in d.items():
    print(k, v)
```

### Output

```python
a 1
b 2
```

---

## pop()

```python
d = {'a':1,'b':2}

d.pop('a')

print(d)
```

### Output

```python
{'b':2}
```

---

# Set Operations

## Create Set

```python
s = set()
```

or

```python
s = {1,2,3}
```

---

## add()

```python
s = {1,2,3}

s.add(4)

print(s)
```

### Output

```python
{1,2,3,4}
```

---

## remove()

```python
s = {1,2,3}

s.remove(2)

print(s)
```

### Output

```python
{1,3}
```

---

## Membership Check

```python
s = {1,2,3}

print(2 in s)
```

### Output

```python
True
```

### Time Complexity

```text
O(1)
```

---

## Union

```python
a = {1,2,3}
b = {3,4,5}

print(a | b)
```

### Output

```python
{1,2,3,4,5}
```

---

## Intersection

```python
a = {1,2,3}
b = {3,4,5}

print(a & b)
```

### Output

```python
{3}
```

---

## Difference

```python
a = {1,2,3}
b = {3,4,5}

print(a - b)
```

### Output

```python
{1,2}
```

---

# enumerate()

Used when both index and value are required.

### Example

```python
arr = [10,20,30]

for i, num in enumerate(arr):
    print(i, num)
```

### Output

```python
0 10
1 20
2 30
```

### Common Interview Use Case

```python
for i, num in enumerate(nums):
```

Used frequently in Two Sum.

---

# zip()

Combines iterables element-wise.

### Example

```python
names = ["Anisha", "Rahul"]
marks = [90, 95]

for name, mark in zip(names, marks):
    print(name, mark)
```

### Output

```python
Anisha 90
Rahul 95
```

---

### Example 2

```python
a = [1,2,3]
b = ['a','b','c']

print(list(zip(a,b)))
```

### Output

```python
[(1,'a'), (2,'b'), (3,'c')]
```

---

# sorted() vs sort()

## sort()

Modifies the original list.

```python
nums = [3,1,2]

nums.sort()

print(nums)
```

### Output

```python
[1,2,3]
```

---

## sorted()

Returns a new sorted object.

```python
nums = [3,1,2]

new_nums = sorted(nums)

print(nums)
print(new_nums)
```

### Output

```python
[3,1,2]
[1,2,3]
```

---

## Interview Question

```python
nums = [3,1,2]

print(nums.sort())
```

### Output

```python
None
```

Because `sort()` modifies the list in-place and returns nothing.

---

# Shallow Copy vs Deep Copy

## Assignment

```python
a = [1,2,3]

b = a

b[0] = 100

print(a)
```

### Output

```python
[100,2,3]
```

Both variables point to the same object.

---

## Shallow Copy

```python
a = [1,2,3]

b = a.copy()

b[0] = 100

print(a)
print(b)
```

### Output

```python
[1,2,3]
[100,2,3]
```

---

## Problem with Nested Lists

```python
a = [[1,2],[3,4]]

b = a.copy()

b[0][0] = 100

print(a)
```

### Output

```python
[[100,2],[3,4]]
```

Inner lists are still shared.

---

## Deep Copy

```python
import copy

a = [[1,2],[3,4]]

b = copy.deepcopy(a)

b[0][0] = 100

print(a)
print(b)
```

### Output

```python
[[1,2],[3,4]]
[[100,2],[3,4]]
```

### Key Difference

* Shallow Copy → Copies outer object only
* Deep Copy → Copies entire nested structure recursively

---

# Interview Cheat Sheet

| Concept      | Description                     |
| ------------ | ------------------------------- |
| get()        | Fetch value safely with default |
| items()      | Returns key-value pairs         |
| Set          | O(1) lookup                     |
| enumerate()  | Returns index and value         |
| zip()        | Combines iterables element-wise |
| sort()       | Sorts list in-place             |
| sorted()     | Returns new sorted iterable     |
| Shallow Copy | Copies outer object only        |
| Deep Copy    | Copies entire nested structure  |
