#Move Zeroes
li=[0,1,0,3,12]
#Output:[1,3,12,0,0]

def moveZeroes(li):
    
    j=0
    for i in range(len(li)):
        if li[i]!=0:
            li[i],li[j]=li[j],li[i]
            print(li)
        
            j+=1
    return li
print(moveZeroes(li))

#Time Complexity
# O(n)

# One pass through the list.

# Space Complexity
# O(1)

# In-place swapping, no extra array.