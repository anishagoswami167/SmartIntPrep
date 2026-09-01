#Remove Adjacent Duplicates
s = "abbaca"
Output="ca"
# Explanation:
# abbaca
# aaca
# ca
#Stack as memory

def remDuplicates(s):
    stack=[]
    res=""
    for n in s:
        if stack and stack[-1]==n:
            stack.pop()
        else:   
            stack.append(n)
        
    return "".join(stack)
print(remDuplicates(s))

# | Time | Space |
# | ---- | ----- |
# | O(n) | O(n)  |


        
            
