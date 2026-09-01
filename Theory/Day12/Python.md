No problem. Let's do **Day 12** step by step and keep it interview-focused.

---

# Python Basics: Decorators & Context Managers

Before understanding decorators, you must understand:

## 1. Functions are Objects

In Python, functions can be:

* Assigned to variables
* Passed as arguments
* Returned from functions

Example:

```python
def greet():
    print("Hello")

say_hello = greet

say_hello()
```

Output:

```python
Hello
```

Notice:

```python
say_hello = greet
```

No parentheses.

We're assigning the function itself.

---

### Interview Question

**Can functions be passed as arguments in Python?**

Yes.

Example:

```python
def greet():
    print("Hello")

def execute(func):
    func()

execute(greet)
```

Output:

```python
Hello
```

---

# 2. Nested Functions

A function inside another function.

```python
def outer():

    def inner():
        print("Inside Inner")

    inner()

outer()
```

Output:

```python
Inside Inner
```

---

# 3. Closures

This is the foundation of decorators.

A closure is:

```text
A nested function that remembers variables
from its outer function even after the outer
function has finished execution.
```

Example:

```python
def outer(msg):

    def inner():
        print(msg)

    return inner

func = outer("Hello")

func()
```

Output:

```python
Hello
```

---

### Why?

Normally:

```python
outer()
```

finishes execution.

But:

```python
inner()
```

still remembers:

```python
msg = "Hello"
```

This remembered state is called a **closure**.

---

### Dry Run

```python
func = outer("Hello")
```

Creates:

```python
msg = "Hello"
```

Returns:

```python
inner
```

Now:

```python
func()
```

actually executes:

```python
inner()
```

which still remembers:

```python
msg = "Hello"
```

Output:

```python
Hello
```

---

# 4. Decorators

## What is a Decorator?

A decorator is a function that adds functionality to another function without modifying the original function.

Think:

```text
Original Function
      ↓
Decorator
      ↓
Enhanced Function
```

---

Example:

```python
def decorator(func):

    def wrapper():
        print("Before Function")

        func()

        print("After Function")

    return wrapper
```

---

Function:

```python
def greet():
    print("Hello")
```

Apply decorator:

```python
greet = decorator(greet)

greet()
```

Output:

```python
Before Function
Hello
After Function
```

---

## Visual

```text
greet()
   ↓
wrapper()
   ↓
Before Function
   ↓
greet()
   ↓
Hello
   ↓
After Function
```

---

# 5. @decorator Syntax

Instead of:

```python
greet = decorator(greet)
```

Python provides:

```python
@decorator
def greet():
    print("Hello")
```

Exactly same result.

Output:

```python
Before Function
Hello
After Function
```

---

# Why Use Decorators?

Very common interview question.

Used for:

```text
Logging
Authentication
Authorization
Timing
Caching
Monitoring
```

---

Example:

```python
@timer
def process_data():
    ...
```

Measures execution time without modifying function.

---

# Context Managers

Another very common interview topic.

---

## Problem

Without context manager:

```python
file = open("data.txt")

data = file.read()

file.close()
```

What if an exception occurs?

```python
file.close()
```

might never run.

File remains open.

---

## Solution

```python
with open("data.txt") as file:

    data = file.read()
```

After block finishes:

```python
file automatically closes
```

---

# What is a Context Manager?

A context manager manages resources automatically.

Examples:

```text
Files
Database Connections
Network Connections
Locks
```

---

# Why Use with open()?

Interview Question

Answer:

```text
with open() automatically closes the file after use,
even if an exception occurs.
This prevents resource leaks and makes code cleaner.
```

---

## Dry Run

```python
with open("data.txt") as file:
    data = file.read()
```

Step 1:

```python
File Opens
```

Step 2:

```python
Read Data
```

Step 3:

Block Ends

```python
File Closes Automatically
```

No need:

```python
file.close()
```

---

# Interview Cheat Sheet

## What is a Closure?

```text
A nested function that remembers variables
from its outer function after the outer
function has completed execution.
```

---

## What is a Decorator?

```text
A function that adds extra functionality
to another function without modifying
its original code.
```

---

## Why Use Decorators?

```text
Logging
Authentication
Caching
Monitoring
Timing
```

---

## What is a Context Manager?

```text
A construct that automatically manages
resources like files and database
connections.
```

---

## Why use with open()?

```text
Automatically closes the file even if
an exception occurs and prevents
resource leaks.
```

---

### Quick Check (Interview Style)

1. What is the difference between a nested function and a closure?

2. What will this print?

```python
def outer():
    x = 10

    def inner():
        print(x)

    return inner

f = outer()
f()
```

3. Why is:

```python
with open()
```

preferred over:

```python
open()
file.close()
```

Answer these in your own words and then we'll move to **Day 12 DSA (Tree DFS)**.
1. Nested Function

A function defined inside another function. Nothing special is being remembered.
def outer():

    def inner():
        print("Hello")

    inner()
Here:

inner() is a nested function

Closure

A closure is:

A nested function that remembers variables
from its outer scope even after the outer
function has finished execution.

Example:

def outer(x):

    def inner():
        print(x)

    return inner

f = outer(10)
f()

Output:

10

Why?

Even though:

outer()

has already finished,

inner()

still remembers:

x = 10

That's what makes it a closure.

3. Why with open()?

Correct ✅

Interview version:

with open() automatically closes the file
after execution, even if an exception occurs,
preventing resource leaks and making code safer.