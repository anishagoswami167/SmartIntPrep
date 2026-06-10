# Approach
# Create a prefix array where each index stores the product of all elements before it.
# Create a suffix array where each index stores the product of all elements after it.
# Multiply prefix and suffix values at each index to get the product of all elements except itself.

# Building Prefix : O(n)
# Building Suffix : O(n)
# Building Result : O(n)

# Total : O(n)

# Prefix Array : O(n)
# Suffix Array : O(n)
# Result Array : O(n)

# Total : O(n)

#Product of Array Except Self
nums=[1,2,3,4]
Output=[24,12,8,6]

def productExceptSelf(nums):

    n = len(nums)

    prefix = [1] * n
    suffix = [1] * n

    # Build prefix array
    for i in range(1, n):
        prefix[i] = prefix[i-1] * nums[i-1]

    # Build suffix array
    for i in range(n-2, -1, -1):
        suffix[i] = suffix[i+1] * nums[i+1]

    # Build answer
    result = [0] * n

    for i in range(n):
        result[i] = prefix[i] * suffix[i]

    return result

print(productExceptSelf(nums))

# Approach

# Store prefix products directly in the result array.
# Traverse from right while maintaining a running suffix product.
# Multiply the current prefix value with the suffix product to get the final answer.
# This avoids creating a separate suffix array.

def productExceptSelf(nums):

    n = len(nums)

    result = [1] * n

    # Prefix products
    for i in range(1, n):
        result[i] = result[i-1] * nums[i-1]

    # Running suffix product
    suffix = 1

    for i in range(n-1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result

#Time Complexity: O(n)
#Space Complexity: O(1)