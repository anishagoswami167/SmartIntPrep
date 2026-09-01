#Remove spaces
strs="hello world"
Output="helloworld"
def removeSpaces(strs):
    clean=""
    for s in strs:
        if s.isalnum():
            clean+=s
    return clean
print(removeSpaces(strs))

# Time:

# O(n)

# Space:

# O(n)

def removeSpaces(strs):

    return strs.replace(" ","")
def removeSpaces(strs):

    return "".join(strs.split())
            
            
            