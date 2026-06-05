Absolutely! Let's start Day 4 with **Python Basics Revision** before jumping into DSA.

Today we'll focus on **Lists and Functions**, because these are used in almost every DSA problem.

---

# 🐍 Python Basics Day 4

## 1. List Operations

### Create List

```python
nums = [10,20,30]
print(nums)
```

Output:

```python
[10,20,30]
```

---

### Append (Add at End)

```python
nums = [10,20,30]

nums.append(40)

print(nums)
```

Output:

```python
[10,20,30,40]
```

### Complexity

```text
Time: O(1)
Space: O(1)
```

---

### Insert

```python
nums = [10,20,30]

nums.insert(1,99)

print(nums)
```

Output:

```python
[10,99,20,30]
```

### Complexity

```text
Time: O(n)
Space: O(1)
```

Because elements need to shift.

---

### Pop

```python
nums = [10,20,30]

nums.pop()

print(nums)
```

Output:

```python
[10,20]
```

Removes last element.

### Complexity

```text
Time: O(1)
Space: O(1)
```

---

## 2. Useful Built-in Functions

### Length

```python
nums = [10,20,30]

print(len(nums))
```

Output:

```python
3
```

---

### Maximum

```python
nums = [10,20,30]

print(max(nums))
```

Output:

```python
30
```

---

### Minimum

```python
nums = [10,20,30]

print(min(nums))
```

Output:

```python
10
```

---

### Sum

```python
nums = [10,20,30]

print(sum(nums))
```

Output:

```python
60
```

---

## 3. Slicing Revision

### First 3 Elements

```python
nums = [10,20,30,40,50]

print(nums[:3])
```

Output:

```python
[10,20,30]
```

---

### Last 2 Elements

```python
print(nums[-2:])
```

Output:

```python
[40,50]
```

---

### Reverse List

```python
print(nums[::-1])
```

Output:

```python
[50,40,30,20,10]
```

---

# 4. Functions Revision

### Simple Function

```python
def greet():
    print("Hello")

greet()
```

Output:

```python
Hello
```

---

### Function with Parameter

```python
def square(n):
    return n*n

print(square(5))
```

Output:

```python
25
```

---

### Multiple Parameters

```python
def add(a,b):
    return a+b

print(add(2,3))
```

Output:

```python
5
```

---

# Mini Exercise 1

Find Maximum Element without using `max()`

Input:

```python
nums = [10,5,20,8]
```

Output:

```python
20
```

Hint:

```python
largest = nums[0]
```

---

# Mini Exercise 2

Find Minimum Element without using `min()`

Input:

```python
nums = [10,5,20,8]
```

Output:

```python
5
```

Hint:

```python
smallest = nums[0]
```

---

# Quick Python Interview Questions

### Q1

Difference between:

```python
append()
```

and

```python
insert()

Method	Time Complexity
append()	O(1)
insert()	O(n)

Because insert shifts elements.
```

---

### Q2

Output?

```python
nums = [1,2,3]

nums.pop()

print(nums)
```

---

### Q3

Output?

```python
nums = [1,2,3,4]

print(nums[::-1])
```

---

### Q4

Difference between:

```python
return
```

and

```python
print()
```

---

### Your Task

Solve these two exercises:

```python
1. Find Maximum Element
2. Find Minimum Element
```

Write:

* Approach
* Time Complexity
* Space Complexity

and send me your code. I'll review it like an interviewer before we move to the Day 4 DSA questions. 🚀
