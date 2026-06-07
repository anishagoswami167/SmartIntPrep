#Maximum Sum Subarray of Size K(Fixed Sliding Window)
arr = [1,2,3,4]
k = 3

#Approach

# Calculate the sum of the first window of size k and initialize it as the maximum sum. 
# Then slide the window one element at a time by removing the leftmost element and adding the new rightmost element. After each slide, update the maximum sum. 
# Finally, return the maximum sum found.

def maxSumSubarray(arr,k):
    window_sum=sum(arr[:k])
    max_sum=window_sum
    left=0
    
    for i in range(k,len(arr)):
        window_sum=window_sum-arr[left]+arr[i]
        left+=1
        max_sum=max(max_sum, window_sum)
    return max_sum
    
print(maxSumSubarray(arr,k))

#Time complexity: O(n)
#sum(arr[:k]) takes O(k), Loop O(n-k), O(k + n-k)=O(n)
#Space Complexity: O(1)

#Brute force
def maxSum(arr, k):

    maxsum = 0

    for i in range(len(arr)-k+1):

        currsum = 0

        for j in range(i, i+k):
            currsum += arr[j]

        maxsum = max(maxsum, currsum)

    return maxsum

#Time complexity: O(n*n)
#Space Complexity: O(1)