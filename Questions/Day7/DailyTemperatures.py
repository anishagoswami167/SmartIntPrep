#Approach
# Create a stack to store indices of temperatures whose next warmer day has not been found yet.
# Traverse the array from left to right.
# For each temperature:
# While the stack is not empty and the current temperature is greater than the temperature at the index stored at the top of the stack:
# Pop the index from the stack.
# Calculate the number of days waited as:
# current_index - popped_index
# Store this value in the result array.
# Push the current index into the stack.
# Any indices left in the stack do not have a warmer temperature in the future, so their result remains 0.

#I use a Monotonic Decreasing Stack to store indices of temperatures whose next warmer day has not yet been found. While traversing the array, whenever the current temperature is greater than the temperature at the top index of the stack, I pop that index and calculate the waiting days as current_index - popped_index. Each index is pushed and popped at most once, giving O(n) time complexity and O(n) space complexity.

#Current temperature is warmer than the temperature at the top index in the stack.

# So that top index has finally found its answer.

# Remove that index from the stack.

# Calculate how many days it waited.

# Store the answer.

#Daily Temperatures
Input=[73,74,75,71,69,72,76,73]
Output=[1,1,4,2,1,1,0,0]

def DailyTemperatures(temp):
    n=len(temp)
    stack=[]
    result=[0]*n
    for i in range(n):
        while stack and temp[i]>temp[stack[-1]]:
            prev=stack.pop()
            result[prev]=i-prev
        stack.append(i)
    return result
print(DailyTemperatures(Input))

#Time Complexity: O(n)
#Space Complexity: O(n)
    