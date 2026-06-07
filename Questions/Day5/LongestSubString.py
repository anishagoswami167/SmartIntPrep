#Longest Substring Without Repeating Characters
s = "abcdefadabcbb"
#Output:4
def longSubstring(s):
    seen=set()
    left=0
    max_len=0

    for i in range(len(s)):
        while s[i] in seen:
            seen.remove(s[i])
            left+=1
        seen.add(s[i])
        max_len=max(max_len,i-left+1)
    return max_len
print(longSubstring(s))