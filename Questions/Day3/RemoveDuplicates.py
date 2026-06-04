#Remove Duplicates from Sorted Array
li=[1,1,2,2,3]
# Output:[1,2,3]

def remDuplicates(li):
    res=[]
    seen=set()
    for i in li:
        if i not in seen:
            seen.add(i)
            res.append(i)
    return res
print(remDuplicates(li))
#Time: O(n)
#Space: O(n)

# Since the array is sorted, duplicate elements will always be adjacent.

# Use two pointers:
# i → points to the last unique element.
# j → scans the array.

# Whenever nums[j] is different from nums[i],
# move i forward and copy nums[j] to that position.

# At the end, all unique elements are stored from index 0 to i.

#Remove Duplicates from Sorted Array
li=[1,1,2,2,3]
# Output:[1,2,3]

def remDuplicates(li):
    i=0
    for j in range(1,len(li)):
       
        if li[i]!=li[j]:
            li[i+1]=li[j]
            i+=1
        print(li)
    return li[:i+1]
            
print(remDuplicates(li))

#Time: O(n)
#Space: O(1)

def remDuplicates(nums):

    i = 0

    for j in range(1, len(nums)):

        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    return nums[:i+1]

print(remDuplicates([1,1,2,2,3]))