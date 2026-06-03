#Check palindrome
l="A man, a plan, a canal: Panama"
Output: True

def palindrome(l):
    
    i=0
    j=len(l)-1
    while i<j:
        while i<j and not l[i].isalnum():
            i+=1
        while i<j and not l[j].isalnum():
             j-=1
        if l[i].lower()!=l[j].lower():
            return False
            
        i+=1
        j-=1
    return True
        
    
print(palindrome(l))
    
        

# Interview Explanation

# A concise explanation:

# We use two pointers, one from the start and one from the end. Before comparing characters, we use inner loops to skip any non-alphanumeric characters such as spaces, commas, or colons. Then we compare the characters in a case-insensitive manner using lower(). If a mismatch is found, we return False. If all comparisons succeed until the pointers cross, we return True.

# Complexity
# Time: O(n)
# Each character is visited at most once by either pointer.
# Space: O(1)
# No extra string is created; only two pointers are used.

# This explanation is usually strong enough for coding interviews.


#Check palindrome
l="A man, a plan, a canal: Panama"
Output: True

def palindrome(l):
    cleaned=""
    for i in l:
        if i.isalnum():
            cleaned+=i.lower()
    print(cleaned)
    return cleaned==cleaned[::-1]
        
    
print(palindrome(l))
    
        

