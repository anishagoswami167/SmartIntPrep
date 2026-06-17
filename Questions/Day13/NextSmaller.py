#Next Smaller Element
nums = [4,8,5,2,25]
Output=[2,5,2,-1,-1]

def nextSmallerEle(nums):
    n=len(nums)
    stack=[]
    result=[-1]*n
    for i in range(n):
        while stack and nums[i]<nums[stack[-1]]:
            prev=stack.pop()
            result[prev]=nums[i]
        stack.append(i)
    return result
    
print(nextSmallerEle(nums))

# | Time | Space |
# | ---- | ----- |
# | O(n) | O(n)  |


