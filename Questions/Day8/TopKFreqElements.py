#Top K Frequent Elements
nums = [1,1,1,2,2,3,4,4,4,4]
k = 2
Output=[1,2]

#BruteForce approach
#First, I build a frequency hashmap. Then I sort the hashmap entries based on frequency in descending order and return the first k elements.
def topKFreqElement(nums, k):

    d = {}
    for n in nums:
        d[n] = d.get(n, 0) + 1

    sorted_items = sorted(
        d.items(),
        key=lambda x: x[1],
        reverse=True
    )

    res = []

    for num, freq in sorted_items[:k]:
        res.append(num)

    return res
        
print(topKFreqElement(nums,k))
#Time Complexity
#Frequency count: O(n)
# Sorting: O(m log m) where m = number of unique elements
# Total: O(n + m log m)
# Space Complexity
# O(m) for hashmap

#Top K Frequent Elements
nums = [1,1,1,2,2,3,4,4,4,4]
k = 2
Output=[1,2]

import heapq

def topKFreqElement(nums, k):

    freq = {}

    for n in nums:
        freq[n] = freq.get(n, 0) + 1

    heap = []

    for num, count in freq.items():
        heapq.heappush(heap, (-count, num))

    res = []

    for _ in range(k):
        count, num = heapq.heappop(heap)
        print(count,num)
        print(heap)
        res.append(num)

    return res
        
print(topKFreqElement(nums,k))


# Excellent question. This is exactly what interviewers ask:

# > "If sorting and heap both are O(n log n), why use a heap?"

# The answer is:

# ### For the solution we just wrote

# Brute Force:

# ```text
# Count Frequency -> O(n)
# Sort -> O(m log m)

# Total = O(n + m log m)
# ```

# Heap Solution (all elements in heap):

# ```text
# Count Frequency -> O(n)
# Push all m elements -> O(m log m)
# Pop k elements -> O(k log m)

# Total ≈ O(n + m log m)
# ```

# ✅ You're right. They are almost the same.

# So what's the point?

# ---

# # The Real Interview Optimization

# Instead of storing ALL elements in the heap, store only K elements.

# Example:

# ```python
# nums = [millions of numbers]
# k = 3
# ```

# Suppose:

# ```text
# Unique elements (m) = 100,000
# ```

# ### Sorting

# Need to sort all 100,000 elements:

# ```text
# O(m log m)
# =
# 100000 × log(100000)
# ```

# ---

# ### Min Heap of Size K

# Keep only:

# ```text
# k = 3
# ```

# elements in the heap.

# Complexity:

# ```text
# O(m log k)
# ```

# which becomes:

# ```text
# O(100000 × log 3)
# ```

# Since:

# ```text
# log 3 ≈ 1.58
# ```

# this is much faster.

# ---

# # Real Numbers

# Suppose:

# ```text
# m = 1,000,000
# k = 10
# ```

# Sorting:

# ```text
# 1,000,000 × log(1,000,000)
# ≈ 20,000,000 operations
# ```

# Heap:

# ```text
# 1,000,000 × log(10)
# ≈ 3,300,000 operations
# ```

# Huge difference.

# ---

# # Interview Flow

# ### Level 1 Answer

# Use sorting.

# ```text
# O(n + m log m)
# ```

# ---

# ### Interviewer asks:

# > Can you optimize?

# ### Level 2 Answer

# Use a heap.

# ```text
# O(n + m log k)
# ```

# This is usually the expected answer.

# ---

# # What You Should Remember

# | Approach                   | Time             |
# | -------------------------- | ---------------- |
# | Sort all frequencies       | O(n + m log m)   |
# | Max Heap with all elements | O(n + m log m)   |
# | Min Heap of size K         | O(n + m log k) ⭐ |

# where:

# ```text
# n = total elements
# m = unique elements
# k = top k required
# ```

# That's why heaps are taught for Top K problems. Not because the basic heap solution is faster than sorting, but because the **optimized heap solution scales much better when k is small and data is huge**.

# This distinction is something many candidates miss in interviews.
