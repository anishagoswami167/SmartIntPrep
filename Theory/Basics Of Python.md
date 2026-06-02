
---

# 1. LIST

A **List** is an ordered collection of items.

```python
fruits = ["apple", "banana", "mango"]
```

### Characteristics

✅ Ordered

✅ Mutable (can change)

✅ Allows duplicates

✅ Supports indexing

---

## Accessing Elements

```python
fruits = ["apple", "banana", "mango"]

print(fruits[0])
```

Output:

```python
apple
```

### Indexing

```python
fruits[0]   # first item
fruits[1]   # second item
fruits[-1]  # last item
```

---

## Length

```python
len(fruits)
```

Output:

```python
3
```

---

## Add Elements

### append()

Adds at end.

```python
fruits.append("orange")

print(fruits)
```

Output:

```python
['apple', 'banana', 'mango', 'orange']
```

---

### insert()

```python
fruits.insert(1, "kiwi")
```

Output:

```python
['apple', 'kiwi', 'banana', 'mango']
```

---

## Remove Elements

### remove()

Removes by value.

```python
fruits.remove("banana")
```

---

### pop()

Removes by index.

```python
fruits.pop(1)
```

---

### pop() without index

Removes last item.

```python
fruits.pop()
```

---

## Update Elements

```python
fruits[0] = "grapes"
```

Output:

```python
['grapes', 'banana', 'mango']
```

---

## Slicing

```python
nums = [1,2,3,4,5]

print(nums[1:4])
```

Output:

```python
[2,3,4]
```

### Meaning

```python
[start:end]
```

Start included

End excluded

---

## Loop Through List

```python
for fruit in fruits:
    print(fruit)
```

---

## Check Existence

```python
if "apple" in fruits:
    print("Found")
```

---

## Sort

```python
nums = [4,1,7,2]

nums.sort()

print(nums)
```

Output:

```python
[1,2,4,7]
```

---

## Reverse

```python
nums.reverse()
```

---

## Common Interview Questions

### Find Largest Number

```python
nums = [4,9,2,7]

print(max(nums))
```

---

### Sum of List

```python
nums = [1,2,3]

print(sum(nums))
```

Output:

```python
6
```

---

# 2. STRING

A String is a sequence of characters.

```python
name = "Anisha"
```

---

## Access Characters

```python
name[0]
```

Output:

```python
A
```

---

## Negative Indexing

```python
name[-1]
```

Output:

```python
a
```

---

## String Slicing

```python
name = "Anisha"

print(name[0:3])
```

Output:

```python
Ani
```

---

## String Length

```python
len(name)
```

Output:

```python
6
```

---

## Upper Case

```python
name.upper()
```

Output:

```python
ANISHA
```

---

## Lower Case

```python
name.lower()
```

Output:

```python
anisha
```

---

## Replace

```python
text = "I love Java"

text.replace("Java", "Python")
```

Output:

```python
I love Python
```

---

## Split

Converts string to list.

```python
sentence = "I love Python"

words = sentence.split()
```

Output:

```python
['I', 'love', 'Python']
```

---

## Join

Converts list to string.

```python
words = ["I", "love", "Python"]

result = " ".join(words)
```

Output:

```python
I love Python
```

---

## Check String

### Startswith

```python
email.startswith("ani")
```

---

### Endswith

```python
email.endswith(".com")
```

---

### Contains

```python
"love" in sentence
```

---

## Reverse String

```python
text = "hello"

print(text[::-1])
```

Output:

```python
olleh
```

---

## Count Character

```python
text = "banana"

text.count("a")
```

Output:

```python
3
```

---

# 3. DICTIONARY

Dictionary stores data in key-value pairs.

```python
student = {
    "name": "Anisha",
    "age": 24,
    "city": "Bangalore"
}
```

---

## Access Value

```python
student["name"]
```

Output:

```python
Anisha
```

---

## Using get()

Safer method.

```python
student.get("name")
```

---

## Add New Key

```python
student["salary"] = 50000
```

---

## Update

```python
student["age"] = 25
```

---

## Delete

```python
del student["city"]
```

---

## Keys

```python
student.keys()
```

Output:

```python
dict_keys(['name', 'age'])
```

---

## Values

```python
student.values()
```

Output:

```python
dict_values(['Anisha', 25])
```

---

## Items

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

## Loop Dictionary

```python
for key, value in student.items():
    print(key, value)
```

---

## Check Key Exists

```python
if "name" in student:
    print("Found")
```

---

## Most Important Interview Pattern

### Count Frequency

```python
text = "banana"

freq = {}

for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)
```

Output:

```python
{
'b':1,
'a':3,
'n':2
}
```

This pattern is extremely important.

---

# 4. SET

A Set stores unique values.

```python
nums = {1,2,3,4}
```

---

## Characteristics

✅ Unordered

✅ No duplicates

✅ Fast lookup

---

## Duplicate Removal

```python
nums = [1,2,2,3,3,4]

unique = set(nums)

print(unique)
```

Output:

```python
{1,2,3,4}
```

---

## Add

```python
s = {1,2,3}

s.add(4)
```

---

## Remove

```python
s.remove(2)
```

---

## Membership Check

Fast operation.

```python
3 in s
```

Output:

```python
True
```

---

## Set Operations

### Union

Combine both sets.

```python
A = {1,2,3}
B = {3,4,5}

print(A | B)
```

Output:

```python
{1,2,3,4,5}
```

---

### Intersection

Common values.

```python
A & B
```

Output:

```python
{3}
```

---

### Difference

```python
A - B
```

Output:

```python
{1,2}
```

---

## Interview Example

### Find Duplicates

```python
nums = [1,2,3,2,4,5,1]

seen = set()
duplicates = set()

for num in nums:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

print(duplicates)
```

Output:

```python
{1,2}
```

---

# Quick Comparison

| Feature    | List | String | Dictionary | Set |
| ---------- | ---- | ------ | ---------- | --- |
| Ordered    | Yes  | Yes    | Yes        | No  |
| Mutable    | Yes  | No     | Yes        | Yes |
| Duplicates | Yes  | Yes    | Keys No    | No  |
| Indexing   | Yes  | Yes    | No         | No  |
| Key-Value  | No   | No     | Yes        | No  |

---

# Must-Know Interview Questions

Practice these until you can solve them without looking:

1. Reverse a string
2. Check palindrome
3. Count character frequency
4. Remove duplicates from list
5. Find largest element
6. Find second largest element
7. Find missing number
8. Merge two dictionaries
9. Find common elements between two lists
10. Group words by frequency
11. Find first non-repeating character
12. Rotate a list
13. Sort dictionary by values
14. Count words in sentence
15. Maximum sum subarray of size K

These problems build directly on Lists, Strings, Dictionaries, and Sets and form the foundation for sliding window, two pointers, hashing, and most coding interview patterns.
