#Check palindrome (Two pointers)
l= "madam"
Output: True

def palindrome(l):
    
    i=0
    j=len(l)-1
    while i<j:
        if l[i]!=l[j]:
            return False
        
        i+=1
        j-=1
    return True
    
print(palindrome(l))    #Time: O(n) Space: O(1)
    
#Slicing       
def palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

l = "mnm"
print(palindrome(l))        #Time: O(n) Space: O(n)
