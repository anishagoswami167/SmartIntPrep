# Problem	Condition
# Consecutive Ones	n == 1
# Consecutive Evens	n % 2 == 0
# Consecutive Positives	n > 0
# Same Number Streak	nums[i] == nums[i-1]

#Maximum Consecutive Ones
nums = [1,1,1,1,1,1,1,0,1,1,1]
#Output:7

def maxCons(nums):
    count=1
    maxcount=1
    for i in range(1,len(nums)):
        if nums[i]==nums[i-1]:
            count+=1
        else:
            count=1
        maxcount = max(maxcount, count)
    return maxcount
    
   
        
    return maxcount
print(maxCons(nums))
    
# Time: O(n)
# Space: O(1)