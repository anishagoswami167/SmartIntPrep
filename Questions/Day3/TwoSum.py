#Two Sum
nums = [2,7,11,15]
target = 9
#Output:[0,1]
            
def twoSum(nums, target):

    r = {}

    for i in range(len(nums)):

        dif = target - nums[i]

        if dif in r:
            return [r[dif], i]

        r[nums[i]] = i

print(twoSum([2,7,11,15], 9))    

# Approach:
# Use a dictionary to store numbers and their indices.

# For each number:
# 1. Calculate complement = target - current number
# 2. Check if complement already exists in dictionary
# 3. If yes, return both indices
# 4. Otherwise store current number and index

#Time Complexity: O(n)
#Space Complexity: O(n)