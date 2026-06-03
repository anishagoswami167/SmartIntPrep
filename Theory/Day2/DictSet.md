Dictionary and Set are among the most important topics for coding interviews because they are based on **hashing**, which helps solve many problems efficiently.

# 1. Dictionary

A dictionary stores data in **key-value pairs**.

```python
student = {
    "name": "Anisha",
    "age": 25,
    "city": "Bangalore"
}
```

Think of it like:

```text
name  -> Anisha
age   -> 25
city  -> Bangalore
```

---

## Why Use Dictionary?

Instead of searching through a list:

```python
students = ["Anisha", "Rahul", "Priya"]
```

You can directly access data using a key:

```python
student["name"]
```

Output:

```python
Anisha
```

---

# Dictionary Characteristics

| Feature          | Dictionary        |
| ---------------- | ----------------- |
| Ordered          | Yes (Python 3.7+) |
| Mutable          | Yes               |
| Duplicate Keys   | Not Allowed       |
| Duplicate Values | Allowed           |
| Indexing         | No                |
| Key-Value Pairs  | Yes               |

---

# Creating Dictionary

### Method 1

```python
student = {
    "name": "Anisha",
    "age": 25
}
```

### Method 2

```python
student = dict(
    name="Anisha",
    age=25
)
```

---

# Access Values

## Using []

```python
student["name"]
```

Output:

```python
Anisha
```

### Problem

```python
student["salary"]
```

Error:

```python
KeyError
```

---

## Using get()

```python
student.get("salary")
```

Output:

```python
None
```

Safer in interviews.

---

# Add New Key

```python
student["salary"] = 50000
```

Result:

```python
{
'name':'Anisha',
'age':25,
'salary':50000
}
```

---

# Update Existing Value

```python
student["age"] = 26
```

---

# Delete

## del

```python
del student["age"]
```

---

## pop()

```python
student.pop("age")
```

Returns removed value.

---

# Keys

```python
student.keys()
```

Output:

```python
dict_keys(['name','age'])
```

---

# Values

```python
student.values()
```

Output:

```python
dict_values(['Anisha',25])
```

---

# Items

```python
student.items()
```

Output:

```python
dict_items([
('name','Anisha'),
('age',25)
])
```

---

# Loop Dictionary

```python
for key, value in student.items():
    print(key, value)
```

Output:

```python
name Anisha
age 25
```

---

# Check Key Exists

```python
if "name" in student:
    print("Found")
```

Output:

```python
Found
```

---

# Most Important Interview Pattern

## Frequency Counter

Input:

```python
banana
```

Output:

```python
{
'b':1,
'a':3,
'n':2
}
```

### Code

```python
text = "banana"

freq = {}

for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)
```

---

# Dry Run

Initial:

```python
freq = {}
```

Character:

```python
'b'
```

```python
freq['b'] = 0 + 1
```

Result:

```python
{'b':1}
```

Character:

```python
'a'
```

```python
{'b':1,'a':1}
```

Continue...

Final:

```python
{'b':1,'a':3,'n':2}
```

---

# Common Dictionary Interview Questions

### Character Frequency

```python
banana
```

---

### Word Frequency

```python
I love Python Python
```

Output:

```python
{
'I':1,
'love':1,
'Python':2
}
```

---

### First Non-Repeating Character

```python
leetcode
```

Output:

```python
l
```

---

### Two Sum

Very famous interview question.

Use dictionary for O(n).

---

# Dictionary Complexity

| Operation | Complexity |
| --------- | ---------- |
| Search    | O(1)       |
| Insert    | O(1)       |
| Delete    | O(1)       |

Average case.

This is why dictionaries are powerful.

---

# 2. SET

A Set stores **unique values**.

```python
s = {1,2,3,4}
```

---

# Characteristics

| Feature     | Set |
| ----------- | --- |
| Ordered     | No  |
| Mutable     | Yes |
| Duplicates  | No  |
| Indexing    | No  |
| Fast Lookup | Yes |

---

# Duplicate Removal

Input:

```python
nums = [1,2,2,3,3,4]
```

Convert:

```python
set(nums)
```

Output:

```python
{1,2,3,4}
```

---

# Create Set

```python
s = {1,2,3}
```

or

```python
s = set([1,2,3])
```

---

# Empty Set

Wrong:

```python
s = {}
```

This creates a dictionary.

Correct:

```python
s = set()
```

---

# Add Element

```python
s.add(5)
```

Output:

```python
{1,2,3,5}
```

---

# Remove Element

```python
s.remove(2)
```

---

# Check Existence

```python
3 in s
```

Output:

```python
True
```

---

# Why Sets Are Fast

Instead of:

```python
nums = [1,2,3,4]

if 4 in nums:
```

List search:

```text
1 → 2 → 3 → 4
```

O(n)

Set search:

```python
4 in s
```

O(1)

---

# Set Operations

Assume:

```python
A = {1,2,3}
B = {3,4,5}
```

---

## Union

All elements.

```python
A | B
```

Output:

```python
{1,2,3,4,5}
```

---

## Intersection

Common elements.

```python
A & B
```

Output:

```python
{3}
```

---

## Difference

```python
A - B
```

Output:

```python
{1,2}
```

---

## Symmetric Difference

Elements in one set but not both.

```python
A ^ B
```

Output:

```python
{1,2,4,5}
```

---

# Most Common Set Interview Question

## Find Duplicates

Input:

```python
[1,2,3,2,4,5,1]
```

Output:

```python
{1,2}
```

### Code

```python
seen = set()
duplicates = set()

for num in nums:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)
```

---

# Dry Run

Input:

```python
[1,2,3,2]
```

Start:

```python
seen = {}
duplicates = {}
```

1:

```python
1 not in seen
```

```python
seen = {1}
```

2:

```python
seen = {1,2}
```

3:

```python
seen = {1,2,3}
```

2 again:

```python
2 in seen
```

```python
duplicates = {2}
```

---

# Dictionary vs Set

| Feature           | Dictionary       | Set         |
| ----------------- | ---------------- | ----------- |
| Stores            | Key-Value        | Values Only |
| Duplicates        | Keys Not Allowed | Not Allowed |
| Lookup            | O(1)             | O(1)        |
| Frequency Count   | Yes              | No          |
| Remove Duplicates | No               | Yes         |

---

# Interview Rule

When solving a problem, ask:

### Need counts/frequencies?

Use **Dictionary**

Example:

```python
banana
```

Need:

```python
a -> 3
n -> 2
```

Use dictionary.

---

### Need uniqueness or fast lookup?

Use **Set**

Example:

```python
[1,2,2,3,3,4]
```

Need:

```python
{1,2,3,4}
```

Use set.

This distinction alone helps solve many string, array, hashing, and interview problems efficiently.
