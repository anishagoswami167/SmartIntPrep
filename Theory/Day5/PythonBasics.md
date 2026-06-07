Welcome back to **Day 5!** 🚀

We'll start with **Python Basics (OOP + List Comprehension)**. Since you're preparing for product companies and GenAI roles, focus on understanding the concepts rather than memorizing definitions.

---

# 🐍 Python Basics – Day 5

## Topic 1: Class and Object

### Real Life Example

Think of a blueprint for a car.

```text
Blueprint = Class
Actual Car = Object
```

---

### Example

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Anisha", 24)

print(s1.name)
print(s1.age)
```

Output:

```python
Anisha
24
```

---

## Understanding Each Line

### Class

```python
class Student:
```

Creates a blueprint.

---

### Constructor

```python
def __init__(self, name, age):
```

Automatically runs when an object is created.

---

### self

```python
self.name = name
```

Means:

```python
This object's name = provided name
```

For example:

```python
s1 = Student("Anisha",24)
```

becomes:

```python
s1.name = "Anisha"
s1.age = 24
```

---

## Interview Question

### What is a Class?

**Answer:**

A class is a blueprint used to create objects.

---

### What is an Object?

**Answer:**

An object is an instance of a class containing actual data.

---

### What is self?

**Answer:**

`self` refers to the current object of the class.

---

# Exercise 1

Write a class:

```python
class Employee
```

Store:

```text
name
salary
```

Create one object and print both values.

---

# Topic 2: Methods Inside Class

```python
class Student:

    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello", self.name)

s = Student("Anisha")

s.greet()
```

Output:

```python
Hello Anisha
```

---

## Interview Question

Difference between:

```python
__init__()
```

and

```python
greet()
```

### Answer

```text
__init__() runs automatically when object is created.

Other methods run only when explicitly called.
```

---

# Topic 3: Inheritance

### Parent Class

```python
class Animal:

    def speak(self):
        print("Animal Sound")
```

---

### Child Class

```python
class Dog(Animal):
    pass
```

---

### Usage

```python
d = Dog()

d.speak()
```

Output:

```python
Animal Sound
```

---

## Why Inheritance?

Without inheritance:

```python
Repeat code
```

With inheritance:

```python
Reuse code
```

---

## Interview Question

What is Inheritance?

**Answer:**

Inheritance allows a child class to reuse properties and methods of a parent class.

---

# Exercise 2

Create:

```python
class Vehicle
```

Method:

```python
start()
```

Create:

```python
class Car(Vehicle)
```

Call:

```python
car.start()
```

---

# Topic 4: List Comprehension

Normal way:

```python
nums = [1,2,3,4]

res = []

for n in nums:
    res.append(n*2)

print(res)
```

Output:

```python
[2,4,6,8]
```

---

### List Comprehension

```python
nums = [1,2,3,4]

res = [n*2 for n in nums]

print(res)
```

Output:

```python
[2,4,6,8]
```

---

## How to Read It

```python
[n*2 for n in nums]
```

means:

```text
Take each n
Multiply by 2
Store in list
```

---

# Exercise 3

Input:

```python
[1,2,3,4,5]
```

Output:

```python
[1,4,9,16,25]
```

Using list comprehension.

---

# Quick Interview Questions

### Q1

Output?

```python
a = [1,2,3]
a.append(4)

print(a)
```

---

### Q2

Output?

```python
a = [1,2,3]
a.pop()

print(a)
```

---

### Q3

Output?

```python
a = [1,2,3]
print(a[::-1])
```

---

### Q4

Difference between:

```python
append()
```

and

```python
extend()
```

append()

Adds a single element.

a=[1,2]
a.append([3,4])

print(a)

Output:

[1,2,[3,4]]

Notice:

Entire list added as ONE element
extend()

Adds each element individually.

a=[1,2]
a.extend([3,4])

print(a)

Output:

[1,2,3,4]
Interview Question

What is the difference?

Answer:

append() adds a single object at the end of the list.

extend() iterates through another iterable and adds its elements individually.



---

# Day 5 Python Deliverables

Complete:

✅ Employee Class

✅ Vehicle → Car Inheritance

✅ Squares using List Comprehension

Answer the 4 interview questions.

Once you send your answers/code, we'll review them and then move to **Day 5 DSA: Maximum Sum Subarray of Size K (Sliding Window)**. 💪
