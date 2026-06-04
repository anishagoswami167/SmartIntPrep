#First Non-Repeating Character
li="eettcodelc"
#Output:"o"

def firstNonRepChar(li):
    res = {}

    for ch in li:
        res[ch] = res.get(ch,0) + 1

    for ch in li:
        if res[ch] == 1:
            return ch
        
    
print(firstNonRepChar(li))


#First two non rep
def firstTwoNonRep(li):
    res = {}

    for ch in li:
        res[ch] = res.get(ch, 0) + 1

    ans = []

    for ch in li:
        if res[ch] == 1:
            ans.append(ch)

        if len(ans) == 2:
            return ans

    return ans

print(firstTwoNonRep("eettcodelc"))