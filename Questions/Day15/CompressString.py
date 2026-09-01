#String compression
strs="aaabbc"
Output="a3b2c1"

def stringCompress(strs):
    count=1
    result=""
    for i in range(1,len(strs)):
        if strs[i]==strs[i-1]:
            count+=1
        else:
            result+=strs[i-1]+str(count)
            count=1
    result+=strs[-1]+str(count)
    return result
print(stringCompress(strs))
