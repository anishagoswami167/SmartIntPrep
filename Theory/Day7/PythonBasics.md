Welcome back! 🚀

Since Day 7 is our **Level-Up Day**, we'll keep Python short and focus only on concepts that actually appear in interviews.

# 🐍 Day 7 Python Basics (20–30 min)

## Topic 1: Lambda Functions

### Normal Function

```python
def square(x):
    return x*x

print(square(5))
```

Output:

```python
25
```

### Lambda Function

```python
square = lambda x: x*x

print(square(5))
```

Output:

```python
25
```

### Interview Answer

> A lambda function is an anonymous one-line function used for short operations. It is useful when we need a function temporarily.

---

## Practice 1

Predict Output:

```python
add = lambda a,b: a+b

print(add(10,20))
```

---

## Topic 2: map()

Used when you want to apply a function to every element.

### Example

```python
nums = [1,2,3,4]

res = list(map(lambda x:x*2, nums))

print(res)
```

Output:

```python
[2,4,6,8]
```

### What's happening?

```text
1 → 2
2 → 4
3 → 6
4 → 8
```

---

## Practice 2

Predict Output:

```python
nums = [1,2,3]

res = list(map(lambda x:x+5, nums))

print(res)
```

---

## Topic 3: filter()

Used when we want to keep only elements satisfying a condition.

### Example

```python
nums = [1,2,3,4,5,6]

res = list(filter(lambda x:x%2==0, nums))

print(res)
```

Output:

```python
[2,4,6]
```

### What's happening?

```text
1 → False → Remove
2 → True  → Keep
3 → False → Remove
4 → True  → Keep
```

---

## Practice 3

Predict Output:

```python
nums = [10,15,20,25]

res = list(filter(lambda x:x>15, nums))

print(res)
```

---

# Topic 4: Exception Handling

### Problem

```python
x = 10/0
```

This gives:

```python
ZeroDivisionError
```

---

### Solution

```python
try:
    x = 10/0
except:
    print("Error occurred")
```

Output:

```python
Error occurred
```

---

### Better Version

```python
try:
    x = 10/0
except Exception as e:
    print(e)
```

Output:

```python
division by zero
```

---

## Interview Question

### Why use try-except?

Answer:

> It prevents the application from crashing when an exception occurs and allows graceful error handling.

---

# Quick Interview Questions

### Q1

Difference between List and Tuple?

### Q2

Difference between map() and filter()?

### Q3

When would you use lambda?

### Q4

What is Exception Handling?

---

# Your Turn

Without running the code, tell me the outputs of:

### Practice 1

```python
add = lambda a,b: a+b

print(add(10,20))
```

### Practice 2

```python
nums = [1,2,3]

res = list(map(lambda x:x+5, nums))

print(res)
```

### Practice 3

```python
nums = [10,15,20,25]

res = list(filter(lambda x:x>15, nums))

print(res)
```

And answer the 4 interview questions. After that we'll move to **DSA Question 1: Valid Parentheses (Stack Pattern)**. 💪
