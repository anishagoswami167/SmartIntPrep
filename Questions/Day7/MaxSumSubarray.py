#Kadane's Algorithm maintains a running sum of the current subarray. 
# If the running sum becomes worse than starting fresh from the current element, 
# we start a new subarray. We keep track of the maximum sum seen so far. 
# This allows us to find the maximum subarray sum in one pass.


# Maximum Subarray Sum (Kadane)
# Input:
# [-2,1,-3,4,-1,2,1,-5,4]
# Output:
# 6

def maxSubArray(nums):

    curr_sum = nums[0]
    max_sum = nums[0]

    for i in range(1, len(nums)):

        curr_sum = max(nums[i], curr_sum + nums[i])

        max_sum = max(max_sum, curr_sum)

    return max_sum

def maxSubArray(nums):

    curr_sum = 0
    max_sum = float('-inf')

    for n in nums:

        curr_sum += n

        max_sum = max(max_sum, curr_sum)

        if curr_sum < 0:
            curr_sum = 0

    return max_sum

#Time Complexity: O(n)
#Space Complexity: O(1)