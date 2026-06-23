#Valid Anagram
s = "abb"
t = "aab"
Output: False

def validAnagram(s,t):
    dic={}
    if len(s)!=len(t):
        return False
    for i in s:
        dic[i]=dic.get(i,0)+1
    for i in t:
        if i not in dic:
            return False
        dic[i]-=1
    for val in dic.values():

        if val != 0:
            return False
    return True
print(validAnagram(s,t))
        