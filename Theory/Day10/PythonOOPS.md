# Python OOP Notes

# What is OOP?

OOP (Object-Oriented Programming) is a programming paradigm that organizes code using:

```text
Classes
Objects
```

Benefits:

* Reusability
* Maintainability
* Scalability
* Better code organization

---

# 1. Class vs Object

## Class

A blueprint/template for creating objects.

Example:

```python
class Employee:
    pass
```

Employee is a class.

---

## Object

An instance of a class.

Example:

```python
class Employee:
    pass

emp1 = Employee()
emp2 = Employee()
```

Here:

```python
emp1
emp2
```

are objects.

---

## Real Life Example

Class:

```text
Car
```

Objects:

```text
BMW
Audi
Mercedes
```

---

# 2. Constructor

A constructor is a special method automatically called when an object is created.

In Python:

```python
__init__()
```

---

## Example

```python
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

emp1 = Employee("Anisha", 50000)

print(emp1.name)
print(emp1.salary)
```

Output:

```python
Anisha
50000
```

---

## self

Represents the current object.

Example:

```python
self.name
```

means:

```python
emp1.name
```

for that particular object.

---

# 3. Inheritance

Inheritance allows one class to acquire properties and methods from another class.

---

## Parent Class

```python
class Employee:

    def work(self):
        print("Working")
```

---

## Child Class

```python
class Manager(Employee):
    pass
```

---

## Example

```python
class Employee:

    def work(self):
        print("Working")


class Manager(Employee):
    pass


m = Manager()

m.work()
```

Output:

```python
Working
```

Manager inherited work() from Employee.

---

## Benefits

* Code Reusability
* Avoid Duplicate Code

---

# 4. Polymorphism

Same method name but different behavior.

---

## Example

```python
class Dog:

    def sound(self):
        print("Bark")


class Cat:

    def sound(self):
        print("Meow")


animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()
```

Output:

```python
Bark
Meow
```

Same method:

```python
sound()
```

Different behavior.

---

## Interview Definition

```text
Polymorphism means one interface, multiple forms.
```

---

# 5. Encapsulation

Encapsulation means hiding internal details and restricting direct access.

---

## Private Variable

```python
class Employee:

    def __init__(self):
        self.__salary = 50000
```

Double underscore:

```python
__salary
```

makes it private.

---

## Example

```python
class Employee:

    def __init__(self):
        self.__salary = 50000

    def get_salary(self):
        return self.__salary


emp = Employee()

print(emp.get_salary())
```

Output:

```python
50000
```

---

## Benefits

* Data Security
* Controlled Access

---

# 6. Static Method

Belongs to the class.

Does NOT use:

```python
self
```

---

## Example

```python
class MathUtils:

    @staticmethod
    def add(a, b):
        return a + b


print(MathUtils.add(2, 3))
```

Output:

```python
5
```

---

## Use Case

Utility functions.

Example:

```python
calculate_tax()
convert_currency()
```

---

# 7. Class Method

Works with class variables.

Uses:

```python
cls
```

instead of:

```python
self
```

---

## Example

```python
class Employee:

    company = "Deloitte"

    @classmethod
    def get_company(cls):
        return cls.company


print(Employee.get_company())
```

Output:

```python
Deloitte
```

---

# Static Method vs Class Method

| Static Method                          | Class Method               |
| -------------------------------------- | -------------------------- |
| Uses @staticmethod                     | Uses @classmethod          |
| No self                                | No self                    |
| No cls                                 | Uses cls                   |
| Cannot access class variables directly | Can access class variables |

---

## Example

```python
class Employee:

    company = "Deloitte"

    @staticmethod
    def greet():
        print("Hello")

    @classmethod
    def get_company(cls):
        return cls.company
```

---

# Interview Questions

### Difference between Class and Object?

Class is a blueprint.
Object is an instance of a class.

---

### What is Constructor?

Special method:

```python
__init__()
```

called automatically during object creation.

---

### What is Inheritance?

Acquiring properties and methods from another class.

---

### What is Polymorphism?

One interface, multiple forms.

---

### What is Encapsulation?

Hiding internal implementation details.

---

### Static Method vs Class Method?

Static Method:

```python
No self
No cls
```

Class Method:

```python
Uses cls
Can access class variables
```
