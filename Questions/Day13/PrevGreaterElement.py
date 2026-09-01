#Previous Greater Element
nums = [15,10,18,12,4,6,2,8]
Output=[-1,15,-1,18,12,12,6,12]

# Logic

# For each number:

# Remove all smaller elements from stack.
# Top of stack will be the nearest greater element.
# Store it in result.
# Push current element into stack.

def prevGreaterEle(nums):
    n=len(nums)
    stack=[]
    result=[]
    for num in nums:
        while stack and stack[-1]<=num:
            stack.pop()
        if stack:
            result.append(stack[-1])
        else:
            result.append(-1)
        stack.append(num)
    return result
    
print(prevGreaterEle(nums))

# | Time | Space |
# | ---- | ----- |
# | O(n) | O(n)  |

