#1. If prefix length is greater than string length, return False.

# 2. Compare each character of prefix with corresponding character in string.

# 3. If any mismatch occurs, return False.

# 4. If all characters match, return True.

#Check Prefix
s = "developer"
pre = "DEV"

def checkPrefix(s,pre):
    if len(pre)>len(s):
        return False
    n=len(pre)
    for i in range(n):
        if s[i].lower()!=pre[i].lower():
            return False
    return True
    
print(checkPrefix(s,pre))

#Time complexity: O(m)  for running pre lopp
#Space Complexity: O(1)