#Stock Span
#Very famous Amazon question.
nums=[100,80,60,70,60,75,85]
Output=[1,1,1,2,1,4,6]
#Learn:Previous Greater Element
#Stock Span = Current Index - Previous Greater Element Index
def stockSpan(nums):
    n=len(nums)
    stack=[]
    result=[]
    for i in range(n):
        
        while stack and nums[stack[-1]]<=nums[i]:
            stack.pop()
            
        if not stack:
            span=i+1
        else:
            span=i-stack[-1]
        result.append(span)
        stack.append(i)
    return result
    

print(stockSpan(nums))

# | Time | Space |
# | ---- | ----- |
# | O(n) | O(n)  |


