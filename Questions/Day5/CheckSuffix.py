#Check Suffix 

s = "developer"
suf= "PER" 


def checkSuffix(s,suf):

    s = s.lower()
    suf = suf.lower()

    if len(suf) > len(s):
        return False

    n = len(suf)

    for i in range(1,n+1):

        if s[-i] != suf[-i]:
            return False

    return True

print(checkSuffix(s,suf))

#Time complexity: O(m)  for running pre lopp
#Space Complexity: O(1)