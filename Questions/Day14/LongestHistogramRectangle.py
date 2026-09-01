# Largest Rectangle in Histogram

nums = [2,1,5,6,2,3]
Output=10
# Difficulty:Hard

#TimeComplexity: O(n)
#SpaceComplexity: O(n)




def largestRectangle(nums):

    n = len(nums)

    # Previous Smaller Index
    prev_small = [-1] * n
    stack = []

    for i in range(n):

        while stack and nums[stack[-1]] >= nums[i]:
            stack.pop()

        if stack:
            prev_small[i] = stack[-1]

        stack.append(i)

    # Next Smaller Index
    next_small = [n] * n
    stack = []

    for i in range(n):

        while stack and nums[stack[-1]] > nums[i]:

            prev = stack.pop()
            next_small[prev] = i

        stack.append(i)

    # Calculate Area
    max_area = 0

    for i in range(n):

        width = next_small[i] - prev_small[i] - 1

        area = nums[i] * width

        max_area = max(max_area, area)

    return max_area


print(largestRectangle(nums))