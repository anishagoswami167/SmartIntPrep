#Count frequency of characters
i="banana"
#Output: {'b':1,'a':3,'n':2}
def countfreq(i):
    res= {}
    count=0
    for j in i:
        if j in res:
            res[j]+=1
        else:
            res[j]=1
    
    return res
    
print(countfreq(i))



#shortcut python
def countfreq(i):
    res = {}

    for ch in i:
        res[ch] = res.get(ch, 0) + 1

    return res

print(countfreq("banana"))