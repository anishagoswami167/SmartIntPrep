#Next Greater Element/Max right (reverse)
nums = [2,1,2,4,3]
Output=[4,2,4,-1,-1]

def nextGreaterEle(nums):
    n=len(nums)
    stack=[]
    result=[-1]*n
    for i in range(n):
        while stack and nums[i]>nums[stack[-1]]:
            prev=stack.pop()
            result[prev]=nums[i]
        stack.append(i)
    return result
    
print(nextGreaterEle(nums))

# | Time | Space |
# | ---- | ----- |
# | O(n) | O(n)  |


#Reverse Order
def nextGreaterElement(nums):

    n = len(nums)

    stack = []

    result = [-1] * n

    for i in range(n - 1, -1, -1):

        while stack and stack[-1] <= nums[i]:
            stack.pop()

        if stack:
            result[i] = stack[-1]

        stack.append(nums[i])

    return result


nums = [2,1,2,4,3]

print(nextGreaterElement(nums))