#Second largest number
nums=[10,5,20,8,7,15,42,67]
Output:10

def secLarge(nums):
    lar=nums[0]
    secLar=0  #float('-inf') represents a number smaller than every possible number. In case there is negative number in list always use float '-inf
    for n in nums:
        if lar<n:
            
            secLar=lar
            lar=n
            
        
        elif secLar<n:
            secLar=n
                
            
                
    return secLar, lar
print(secLarge(nums))


#With Max
nums = [10,5,20,8,7,15,42,67]

largest = max(nums)

nums.remove(largest)

second_largest = max(nums)

print(second_largest)

#With sort
nums = [10,5,20,8,7,15,42,67]

nums.sort()

largest = nums[-1]
second_largest = nums[-2]

print(second_largest, largest)
        