Great. Let's finish the remaining **Day 9 Python Interview Concepts** before moving to DSA.

# 1. `collections.Counter`

### What is it?

A specialized dictionary used for frequency counting.

### Example

```python
from collections import Counter

nums = [1,1,2,2,2,3]

c = Counter(nums)

print(c)
```

Output:

```python
Counter({2: 3, 1: 2, 3: 1})
```

---

### Equivalent Normal Dictionary

```python
d = {}

for n in nums:
    d[n] = d.get(n, 0) + 1
```

---

### Most Common Elements

```python
from collections import Counter

nums = [1,1,1,2,2,3]

c = Counter(nums)

print(c.most_common(2))
```

Output:

```python
[(1,3),(2,2)]
```

Interview use:

* Top K Frequent Elements
* Top K Frequent Words
* Frequency Problems

---

# 2. defaultdict

### Problem

```python
d = {}

d["a"].append(1)
```

Error:

```python
KeyError
```

because `"a"` doesn't exist.

---

### Solution

```python
from collections import defaultdict

d = defaultdict(list)

d["a"].append(1)

print(d)
```

Output:

```python
defaultdict(<class 'list'>, {'a': [1]})
```

---

### Interview Use Case: Group Anagrams

Without defaultdict:

```python
if key not in d:
    d[key] = []

d[key].append(word)
```

With defaultdict:

```python
from collections import defaultdict

d = defaultdict(list)

d[key].append(word)
```

Cleaner code.

---

# 3. OrderedDict

### Purpose

Maintains insertion order.

```python
from collections import OrderedDict

d = OrderedDict()

d["a"] = 1
d["b"] = 2

print(d)
```

Output:

```python
OrderedDict([('a',1), ('b',2)])
```

---

### Interview Use

Most commonly:

```text
LRU Cache
```

questions.

---

### Modern Python Note

Since Python 3.7+:

```python
dict
```

already preserves insertion order.

So OrderedDict is less commonly used now.

---

# 4. enumerate()

### Problem

Need both index and value.

Without enumerate:

```python
nums = [10,20,30]

for i in range(len(nums)):
    print(i, nums[i])
```

---

### Better

```python
nums = [10,20,30]

for i, n in enumerate(nums):
    print(i, n)
```

Output:

```python
0 10
1 20
2 30
```

---

### Interview Use

Two Sum

```python
for i, n in enumerate(nums):
```

Very common.

---

# 5. zip()

### Purpose

Iterate through multiple lists together.

Example:

```python
names = ["Anisha","Rahul"]
scores = [90,95]

for name, score in zip(names, scores):
    print(name, score)
```

Output:

```python
Anisha 90
Rahul 95
```

---

### Interview Use

Combining two arrays.

---

# 6. sorted() vs sort()

### sort()

Changes original list.

```python
nums = [3,1,2]

nums.sort()

print(nums)
```

Output:

```python
[1,2,3]
```

---

### sorted()

Returns a new list.

```python
nums = [3,1,2]

new_nums = sorted(nums)

print(new_nums)
```

Output:

```python
[1,2,3]
```

Original:

```python
[3,1,2]
```

remains unchanged.

---

# 7. Lambda Functions

### Normal Function

```python
def square(x):
    return x*x
```

---

### Lambda

```python
square = lambda x: x*x
```

---

### Sorting Example

```python
items = [('a',3), ('b',1), ('c',2)]

sorted_items = sorted(
    items,
    key=lambda x: x[1]
)
```

Output:

```python
[('b',1), ('c',2), ('a',3)]
```

---

# 8. Mutable vs Immutable

### Mutable

Can be modified.

Examples:

```python
list
dict
set
```

```python
nums = [1,2,3]

nums.append(4)
```

Valid.

---

### Immutable

Cannot be modified.

Examples:

```python
str
tuple
int
float
```

```python
s = "hello"

s[0] = "H"
```

Error.

---

# 9. Shallow Copy vs Deep Copy

### Shallow Copy

```python
import copy

a = [[1,2],[3,4]]

b = copy.copy(a)
```

Outer list copied.

Inner lists still shared.

---

### Deep Copy

```python
import copy

a = [[1,2],[3,4]]

b = copy.deepcopy(a)
```

Everything copied independently.

---

### Interview Example

```python
import copy

a = [[1,2],[3,4]]

b = copy.copy(a)

b[0][0] = 100

print(a)
```

Output:

```python
[[100,2],[3,4]]
```

Because inner list is shared.

---

# Python Interview Cheat Sheet

| Concept      | Use                      |
| ------------ | ------------------------ |
| Counter      | Frequency counting       |
| defaultdict  | Auto-create missing keys |
| OrderedDict  | LRU Cache                |
| enumerate    | Index + Value            |
| zip          | Multiple list traversal  |
| sort()       | Modify original          |
| sorted()     | New sorted list          |
| lambda       | Anonymous function       |
| Mutable      | List, Dict, Set          |
| Immutable    | String, Tuple, Int       |
| Shallow Copy | Copies outer object      |
| Deep Copy    | Copies everything        |

### Quick Check (answer without coding)

1. Which is faster for lookup: List or Set?
2. What does `enumerate()` return?
3. When would you use `defaultdict(list)`?
4. Difference between `sort()` and `sorted()`?



1. Which is faster for lookup?

Your Answer:

Set

✅ Correct

Reason:

List Lookup  → O(n)
Set Lookup   → O(1)

Because sets use hashing internally.

2. What does enumerate() return?

Your Answer:

index and values

✅ Correct

Example:

nums = [10,20,30]

for i,n in enumerate(nums):
    print(i,n)

Output:

0 10
1 20
2 30
3. When would you use defaultdict(list)?

Your Answer:

append the ele with key and value

✅ Correct idea.

Interview Answer:

defaultdict(list) automatically creates an empty list for a missing key, making it useful for grouping data.

Example:

from collections import defaultdict

d = defaultdict(list)

d["a"].append(1)

Common uses:

Group Anagrams
Graph Adjacency Lists
Grouping records by category
4. sort() vs sorted()

Your Answer:

sort() modifies original list and returns None. sorted() returns a new sorted list.

