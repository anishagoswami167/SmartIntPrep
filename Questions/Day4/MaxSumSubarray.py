# Ahh, now I understand. You're asking:

# > **How do I explain the problem-solving thought process from Brute Force → Sliding Window in an interview?**

# This is actually what interviewers love to hear.

# ---

# # Problem

# ```python
# arr = [2,1,5,1,3,2]
# k = 3
# ```

# Find maximum sum subarray of size `k`.

# ---

# # Step 1: Brute Force Thinking

# ### My first thought

# Generate every subarray of size `k`.

# ```text
# [2,1,5]
# [1,5,1]
# [5,1,3]
# [1,3,2]
# ```

# Calculate sum of each.

# Keep track of maximum.

# ---

# ### Brute Force Code

# ```python
def maxSum(arr, k):

    maxsum = 0

    for i in range(len(arr)-k+1):

        currsum = 0

        for j in range(i, i+k):
            currsum += arr[j]

        maxsum = max(maxsum, currsum)

    return maxsum
# ```

# ---

# ### Interview Explanation

# ```text
# 1. Start from every possible index.
# 2. Calculate sum of next k elements.
# 3. Compare with maximum sum.
# 4. Return maximum.
# ```

# ---

# ### Time Complexity

# Outer loop:

# ```text
# O(n)
# ```

# Inner loop:

# ```text
# O(k)
# ```

# Total:

# ```text
# O(n*k)
# ```

# Space:

# ```text
# O(1)
# ```

# ---

# # Step 2: Observe the Problem

# Now as an interviewer, I would say:

# ```text
# Can we optimize it?
# ```

# Look at these windows:

# ```text
# [2,1,5] = 8

# [1,5,1] = 7

# [5,1,3] = 9

# [1,3,2] = 6
# ```

# Notice:

# ```text
# Window 1:
# 2 1 5

# Window 2:
#   1 5 1
# ```

# We are recalculating:

# ```text
# 1
# 5
# ```

# again.

# That's repeated work.

# ---

# # Key Observation

# To move from:

# ```text
# [2,1,5]
# ```

# to

# ```text
# [1,5,1]
# ```

# We only:

# ```text
# Remove 2
# Add 1
# ```

# Everything else remains same.

# ---

# # Sliding Window Thought Process

# Instead of:

# ```text
# Recalculate sum of all k elements
# ```

# Let's reuse previous sum.

# Formula:

# ```python
# new_sum = old_sum - outgoing + incoming
# ```

# ---

# # Example

# First window:

# ```text
# [2,1,5]
# ```

# Sum:

# ```text
# 8
# ```

# ---

# Next window:

# ```text
# [1,5,1]
# ```

# Instead of:

# ```python
# 1+5+1
# ```

# Do:

# ```python
# 8 - 2 + 1
# ```

# Result:

# ```text
# 7
# ```

# ---

# Next:

# ```text
# [5,1,3]
# ```

# Do:

# ```python
# 7 - 1 + 3
# ```

# Result:

# ```text
# 9
# ```

# ---

# # Sliding Window Code

# ```python
def maxSum(arr, k):

    window_sum = sum(arr[:k])

    max_sum = window_sum

    for i in range(k, len(arr)):

        window_sum = window_sum - arr[i-k] + arr[i]

        max_sum = max(max_sum, window_sum)

    return max_sum


# ---

# # Interview Explanation

# ```text
# 1. Calculate sum of first window of size k.

# 2. Slide the window one step at a time.

# 3. Remove the leftmost element.

# 4. Add the new rightmost element.

# 5. Update maximum sum.

# 6. Return maximum sum.
# ```

# ---

# # Complexity Comparison

# | Approach       | Time   | Space |
# | -------------- | ------ | ----- |
# | Brute Force    | O(n*k) | O(1)  |
# | Sliding Window | O(n)   | O(1)  |

# ---

# # What Interviewers Want To Hear

# A strong answer is:

# ```text
# My initial brute force approach is to generate every subarray of size k and calculate its sum, which takes O(n*k) time.

# However, I noticed that adjacent windows overlap significantly. Instead of recalculating the entire sum, I can reuse the previous window sum by subtracting the outgoing element and adding the incoming element.

# This leads to the Sliding Window approach with O(n) time complexity and O(1) space complexity.
# ```

# This explanation is often more important than the code itself because it shows your optimization thinking.

# ---

# ### Sliding Window Recognition Rule

# Whenever you see:

# ```text
# Subarray of size K
# Substring of size K
# Maximum sum of K elements
# Average of K elements
# ```

# Immediately think:

# ```text
# Fixed Size Sliding Window
# ```

# That's the pattern interviewers expect you to recognize. 🚀
