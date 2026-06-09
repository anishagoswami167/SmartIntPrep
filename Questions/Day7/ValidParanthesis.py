# Interview Explanation

# Approach:

# Use a stack to store opening brackets.
# For every closing bracket, check whether the top of the stack contains the corresponding opening bracket.
# If not, return False.
# At the end, if the stack is empty, all brackets are matched.

#Time Complexity: O(n)
#Space Complexity: O(n)

#Valid Parentheses
Input="()[]{}"
Output=True

def validParanthesis(br):
    stack=[]
    p={
        ')':'(',
        ']':'[',
        '}':'{'
    }
    for b in br:
        if b in "({[":
            stack.append(b)
        else:
            if not stack:
                return False
            if stack[-1]==p[b]:
                stack.pop()
            else:
                return False
    return len(stack) == 0
print(validParanthesis(Input))
            
