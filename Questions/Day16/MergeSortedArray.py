# Merge two sorted arrays
# Input
ar1=[1,3,5]
ar2=[2,4,6]
Output=[1,2,3,4,5,6]

def mergeSortArray(ar1,ar2):
    res=[]
    i=0
    j=0
    while i<len(ar1) and j<len(ar2):
        if ar1[i]<ar2[j]:
            res.append(ar1[i])
            i+=1
        else:
            res.append(ar2[j])
            j+=1
    
    while i < len(ar1):

        res.append(ar1[i])
        i += 1

    while j < len(ar2):

        res.append(ar2[j])
        j += 1
    return res
    
print(mergeSortArray(ar1,ar2))

#Complexity
#Time=O(m+n)
#Space=O(m+n)