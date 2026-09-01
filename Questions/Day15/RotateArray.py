# Let's use:

# ```python
# arr = [1,2,3,4,5]
# k = 2
# ```

# Output:

# ```python
# [3,4,5,1,2]
# ```

# ---

# Method 1: Rotate One Step K Times (Brute Force)

### Time: O(n*k)

### Space: O(1)

def leftRotateBrute(arr, k):

    n = len(arr)

    for _ in range(k):

        first = arr[0]

        for i in range(n-1):
            arr[i] = arr[i+1]

        arr[-1] = first

    return arr

arr = [1,2,3,4,5]
print(leftRotateBrute(arr, 2))

# Method 2: Extra Array / Slicing

### Time: O(n)

### Space: O(n)


def leftRotateExtra(arr, k):

    n = len(arr)

    k = k % n

    return arr[k:] + arr[:k]

arr = [1,2,3,4,5]
print(leftRotateExtra(arr, 2))

# Method 3: Reversal Algorithm (Optimal)

### Time: O(n)

### Space: O(1)


def reverse(arr, l, r):

    while l < r:

        arr[l], arr[r] = arr[r], arr[l]

        l += 1
        r -= 1


def leftRotateOptimal(arr, k):

    n = len(arr)

    k = k % n

    reverse(arr, 0, k-1)

    reverse(arr, k, n-1)

    reverse(arr, 0, n-1)

    return arr


arr = [1,2,3,4,5]
print(leftRotateOptimal(arr, 2))

# # Interview Summary

# | Method                | Time   | Space  |
# | --------------------- | ------ | ------ |
# | Rotate 1 step K times | O(n*k) | O(1)   |
# | Extra Array/Slicing   | O(n)   | O(n)   |
# | Reversal Algorithm    | O(n)   | O(1) ✅ |

# For interviews:

# * Brute force → explain first.
# * Extra array → easy optimization.
# * Reversal algorithm → best answer if interviewer asks for optimal solution.
