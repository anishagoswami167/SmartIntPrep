#Longest Subarray with Sum K (Variable Sliding Window)
#Use a sliding window.

# Expand the window by moving the right pointer.

# If the sum exceeds k, shrink the window from the left until the sum becomes less than or equal to k.

# Whenever the sum equals k, update the maximum length.
arr = [1,2,3,1,1,1,1,1]
k = 5
#Output:5

def longestSubarray(arr, k):
    left=0
    max_len=0
    cur_sum=0
    for i in range(len(arr)):
        cur_sum+=arr[i]
        
        while k<cur_sum:
            cur_sum-=arr[left]
            left+=1
        if k==cur_sum:
            max_len=max(max_len, i-left+1)
    return max_len



print(longestSubarray(arr, k))

#Time complexity: O(n)
#Space Complexity: O(1)



