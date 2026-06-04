| Data Type  | Add Element         |
| ---------- | ------------------- |
| List       | `append()`          |
| String     | `+` or `+=`         |
| Set        | `add()`             |
| Dictionary | `dict[key] = value` |


Welcome back! 🚀

Day 3 starts with strengthening Python fundamentals because strong Python makes DSA much easier.

# 🐍 Day 3 - Python Basics Revision (30-40 mins)

Today's focus:

```text
Lists
Strings
List Comprehension
Built-in Functions
```

---

# 1. List Operations

## Create List

```python
arr = [1,2,3,4]
print(arr)
```

Output:

```python
[1,2,3,4]
```

---

## Append Element

```python
arr = [1,2,3]

arr.append(4)

print(arr)
```

Output:

```python
[1,2,3,4]
```

### Complexity

```text
Time: O(1)
Space: O(1)
```

---

## Remove Element

```python
arr = [1,2,3,4]

arr.remove(2)

print(arr)
```

Output:

```python
[1,3,4]
```

### Complexity

```text
Time: O(n)
```

Python searches for the element first.

---

## Length

```python
arr = [1,2,3,4]

print(len(arr))
```

Output:

```python
4
```

---

# 2. List Slicing

## First 3 Elements

```python
arr = [10,20,30,40,50]

print(arr[:3])
```

Output:

```python
[10,20,30]
```

---

## Last 2 Elements

```python
arr = [10,20,30,40,50]

print(arr[-2:])
```

Output:

```python
[40,50]
```

---

## Reverse List

```python
arr = [1,2,3,4,5]

print(arr[::-1])
```

Output:

```python
[5,4,3,2,1]
```

---

# 3. String Basics

## Reverse String

```python
s = "python"

print(s[::-1])
```

Output:

```python
nohtyp
```

---

## Upper Case

```python
s = "python"

print(s.upper())
```

Output:

```python
PYTHON
```

---

## Lower Case

```python
s = "PYTHON"

print(s.lower())
```

Output:

```python
python
```

---

# 4. Split

Convert string into list.

```python
sentence = "I love coding"

words = sentence.split()

print(words)
```

Output:

```python
['I', 'love', 'coding']
```

---

# 5. Join

Convert list into string.

```python
words = ['I','love','coding']

result = " ".join(words)

print(result)
```

Output:

```python
I love coding
```

---

# 6. List Comprehension

Instead of:

```python
nums = [1,2,3,4]

squares = []

for n in nums:
    squares.append(n*n)

print(squares)
```

Use:

```python
nums = [1,2,3,4]

squares = [n*n for n in nums]

print(squares)
```

Output:

```python
[1,4,9,16]
```

---

# 7. max(), min(), sum()

```python
nums = [10,5,20,8]

print(max(nums))
print(min(nums))
print(sum(nums))
```

Output:

```python
20
5
43
```

---

# ✍️ Mini Exercise 1

Count Vowels

Input:

```python
banana
```

Output:

```python
3
```

Try solving yourself:

```python
s = "banana"

def countVowels(s):
    pass

print(countVowels(s))
```

---

# ✍️ Mini Exercise 2

Reverse String

Input:

```python
python
```

Output:

```python
nohtyp
```

Try without using:

```python
[::-1]
```

Hint:

```python
for loop
```

---

# Quick Revision Questions

Without running code, tell me the output:

### Q1

```python
arr = [10,20,30,40]

print(arr[-1])
```

---

### Q2

```python
s = "Python"

print(s[1:4])
```

---

### Q3

```python
words = ['I','love','AI']

print("-".join(words))
```

---

### Q4

```python
nums = [1,2,3]

result = [x*2 for x in nums]

print(result)
```

---

Complete:

1. Count Vowels
2. Reverse String (without slicing)
3. Q1-Q4 outputs

Then we'll move to **Day 3 DSA Question 1: Remove Duplicates from Sorted Array**. 🚀
