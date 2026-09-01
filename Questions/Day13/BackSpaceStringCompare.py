 #Backspace String Compare
so = "ab#c"
to = "ad#c"
Output=True
# means pop

def backspaceCompare(so,to):
    stack1=[]
    stack2=[]
    for s in so:
        if s=="#":
            stack1.pop()
        else:
            stack1.append(s)
    for t in to:
        if t=="#":
            stack2.pop()
        else:
            stack2.append(t)
    return stack1==stack2
print(backspaceCompare(so,to))


def build(string):

    stack = []

    for ch in string:

        if ch == "#":
            if stack:
                stack.pop()
        else:
            stack.append(ch)

    return stack


def backspaceCompare(s, t):

    return build(s) == build(t)


print(backspaceCompare("ab#c", "ad#c"))

# Complexity
# Time
# O(n + m)

# where:

# n = length of first string
# m = length of second string
# Space
# O(n + m)

# for stacks.