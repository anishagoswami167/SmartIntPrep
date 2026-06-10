#Binary Search Variations
#First Occurence Position
nums = [1,2,2,2,3]
target = 2
Output=1

def BinarySearch(nums,target):
    left=0
    right=len(nums)-1
    res=0
    
    while left<=right:
        mid=(right+left)//2
        if nums[mid]==target:
            res=mid
            right=mid-1
        elif nums[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return res
    
print(BinarySearch(nums,target))


#Binary Search Variations
#Last Occurence Position
nums = [1,2,2,2,3]
target = 3
Output=1

def BinarySearch(nums,target):
    left=0
    right=len(nums)-1
    res=0
    
    while left<=right:
        mid=(right+left)//2
        if nums[mid]==target:
            res=mid
            left=mid+1
        elif nums[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return res
    
print(BinarySearch(nums,target))

# Time Complexity
# O(log n)

# Because search space is halved every iteration.

# Space Complexity
# O(1)

# No extra space used.