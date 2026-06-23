#Check rotation of string
s1="ABCD"
s2="CDAB"
Output=True

#1. Concatenation Method
def checkRotation(s1,s2):
    if len(s1)!=len(s2):
        return False
    return s2 in s1+s1
print(checkRotation(s1,s2))

#2. Cyclic Comparison
#Check rotation of string
s1="ABCD"
s2="CDAB"
Output=True

def checkRotation(s1,s2):
    if len(s1)!=len(s2):
        return False
    return s2 in s1+s1
print(checkRotation(s1,s2))

#3. Generate All Rotations
def checkRotation(s1,s2):

    if len(s1)!=len(s2):
        return False

    temp=s1

    for i in range(len(s1)):

        if temp==s2:
            return True

        temp=temp[1:]+temp[0]

    return False

#What I Would Say In Interview

# Brute force is to generate all rotations and compare. An optimized solution uses the fact that if s2 is a rotation of s1, then s2 must appear in s1+s1. Therefore, I simply check whether s2 is a substring of s1+s1 after verifying both strings have equal length.

# That's usually the answer interviewers expect. ✅