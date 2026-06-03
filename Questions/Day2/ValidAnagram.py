#Valid Anagram
s = "listen"
t = "silent"
Output: True

def anagram(s,t):
    res={}
    if len(s)!=len(t):
        return False
    for n in s:
        res[n]= res.get(n,0)+1
        # print(res)
    for ch in t:
        if ch not in res:
            return False
        res[ch]-=1
        print(res)
    return True
print(anagram(s,t))
