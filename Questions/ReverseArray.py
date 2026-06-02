#Reverse an array
n=[1,2,3,4,5]
Output=[5,4,3,2,1]

def reverse(n):
    res=n[::-1]
    return res

print(reverse(n))  #Time: O(n) Space: O(n)

#Reverse an array
n=[1,2,3,4,5,8]
Output=[5,4,3,2,1]

# Two pointers approach
def reverse(n):
    j=len(n)-1
    i=0
    while i<j:
        n[i],n[j]=n[j],n[i]         #Swapping
        i+=1
        j-=1
    return n
        
        
print(reverse(n))

#Time Complexity: O(n), because we traverse approximately half the array and perform constant-time swaps.
#Space Complexity: O(1), because the reversal is done in-place using only two pointer variables.