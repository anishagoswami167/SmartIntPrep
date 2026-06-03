#Largest element (without sort and max function)

def largest(num):
    m = num[0]

    for i in range(len(num)):
        if num[i] > m:
            m = num[i]

    return m

num = [4,8,1,10,122,19,97]
print(largest(num))


#| Approach                   | Time       | Space                                    |
# | -------------------------- | ---------- | ---------------------------------------- |
# | `max(num)`                 | O(n)       | O(1)                                     |
# | `sort()` then last element | O(n log n) | O(1) or O(n) depending on implementation |
# | Traversal (your approach)  | O(n)       | O(1) ✅                                  |

# If asked:

# Why is traversal better than sorting?

# You can say:

# "Sorting takes O(n log n) time, while finding the maximum element only requires one pass through the array, which takes O(n) time and O(1) extra space."
