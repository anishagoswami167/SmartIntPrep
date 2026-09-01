Perfect. Let's start **Day 11 Python** in the same notes format you can save directly to GitHub.

# Day 11 - Python Advanced Concepts

# 1. Iterable

## Definition

An Iterable is any object that can be looped over using:

```python
for item in object:
```

Examples:

```python
list
tuple
string
dictionary
set
```

Example:

```python
nums = [1,2,3]

for n in nums:
    print(n)
```

Output:

```python
1
2
3
```

---

# 2. Iterator

## Definition

An Iterator is an object that remembers its state and returns one element at a time.

Uses:

```python
next()
```

Internally implements:

```python
__iter__()
__next__()
```

---

## Example

```python
nums = [1,2,3]

it = iter(nums)

print(next(it))
print(next(it))
print(next(it))
```

Output:

```python
1
2
3
```

---

## What happens next?

```python
print(next(it))
```

Output:

```python
StopIteration
```

---

# Iterable vs Iterator

| Iterable                 | Iterator                   |
| ------------------------ | -------------------------- |
| Collection of values     | Produces values one by one |
| Uses iter()              | Uses next()                |
| Cannot remember position | Remembers current position |

Example:

```python
nums = [1,2,3]
```

Iterable:

```python
nums
```

Iterator:

```python
iter(nums)
```

---

# 3. Generator

## Definition

A Generator is a special type of Iterator created using:

```python
yield
```

It generates values one at a time instead of storing everything in memory.

---

## Example

```python
def generate_numbers():

    yield 1
    yield 2
    yield 3

g = generate_numbers()

print(next(g))
print(next(g))
print(next(g))
```

Output:

```python
1
2
3
```

---

## Why Generators?

Normal Function:

```python
def nums():
    return [1,2,3]
```

Creates entire list in memory.

Generator:

```python
def nums():
    yield 1
    yield 2
    yield 3
```

Creates values only when needed.

Memory Efficient.

---

# 4. yield

## Definition

yield pauses the function and remembers its state.

Next call resumes from where it stopped.

---

## Example

```python
def count():

    yield 1
    yield 2
    yield 3

g = count()

print(next(g))
print(next(g))
print(next(g))
```

Output:

```python
1
2
3
```

---

## Flow

```text
yield 1
pause

next()
resume

yield 2
pause

next()
resume

yield 3
```

---

# return vs yield

## return

```python
def func():
    return 1
```

Function ends immediately.

---

## yield

```python
def func():
    yield 1
```

Function pauses and can continue later.

---

## Interview Answer

```text
return terminates the function.

yield pauses the function and preserves state.
```

---

# 5. next()

Used to get the next value from an iterator or generator.

Example:

```python
nums = [1,2,3]

it = iter(nums)

print(next(it))
```

Output:

```python
1
```

---

# 6. *args

## Definition

Allows passing variable number of positional arguments.

---

## Example

```python
def add(*args):

    print(args)

add(1,2,3,4)
```

Output:

```python
(1,2,3,4)
```

Tuple is created.

---

## Sum Example

```python
def add(*args):

    return sum(args)

print(add(1,2,3))
```

Output:

```python
6
```

---

# 7. **kwargs

## Definition

Allows passing variable number of keyword arguments.

---

## Example

```python
def details(**kwargs):

    print(kwargs)

details(name="Anisha", age=25)
```

Output:

```python
{
'name':'Anisha',
'age':25
}
```

Dictionary is created.

---

# *args vs **kwargs

| *args                | **kwargs          |
| -------------------- | ----------------- |
| Positional Arguments | Keyword Arguments |
| Tuple                | Dictionary        |

Example:

```python
def demo(*args, **kwargs):
    pass
```

---

# 8. Decorators (Introduction)

## Definition

A Decorator is a function that modifies the behavior of another function without changing its code.

---

## Example

```python
def decorator(func):

    def wrapper():
        print("Before Function")

        func()

        print("After Function")

    return wrapper
```

---

## Applying Decorator

```python
@decorator
def greet():

    print("Hello")
```

Equivalent to:

```python
greet = decorator(greet)
```

---

## Output

```python
Before Function
Hello
After Function
```

---

# Why Decorators?

Used for:

```python
Logging
Authentication
Authorization
Timing Functions
Caching
Monitoring
```

Very common in:

```python
Flask
FastAPI
Django
```

---

# Interview Questions

## Difference between Iterator and Generator?

Iterator:

```text
Uses iter() and next().
```

Generator:

```text
Uses yield and automatically creates an iterator.
```

---

## Difference between return and yield?

return:

```text
Terminates function.
```

yield:

```text
Pauses function and resumes later.
```

---

## Why use Generators?

```text
Memory Efficient.
Generates values lazily.
Useful for large datasets.
```

---

## What are Decorators?

```text
Functions that modify another function's behavior without changing its source code.
```

---

## Difference between *args and **kwargs?

*args:

```text
Variable positional arguments.
Stored as Tuple.
```

**kwargs:

```text
Variable keyword arguments.
Stored as Dictionary.
```

# Quick Revision

```text
Iterable
    ↓
Iterator
    ↓
next()
    ↓
Generator
    ↓
yield
    ↓
*args
    ↓
**kwargs
    ↓
Decorators
```

### Mini Interview Question

What will be the output?

```python
def gen():
    yield 10
    yield 20

g = gen()

print(next(g))
print(next(g))
```

1. Output?
2. Why is `gen()` called a Generator?
3. What happens if we call `next(g)` one more time?
