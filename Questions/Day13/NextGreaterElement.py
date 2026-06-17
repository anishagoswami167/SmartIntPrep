#Next Greater Element
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

