#1. Brute Force
def trappingRainWater_bruteforce(height):

    n = len(height)
    water = 0

    for i in range(n):

        left_max = max(height[:i+1])

        right_max = max(height[i:])

        water += min(left_max, right_max) - height[i]

    return water


height = [0,1,0,2,1,0,1,3,2,1,2,1]

print(trappingRainWater_bruteforce(height))

#Storing left and right max in arrays
def trappingRainWater_prefix(height):

    n = len(height)

    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = height[0]

    for i in range(1, n):
        left_max[i] = max(left_max[i-1], height[i])

    right_max[n-1] = height[n-1]

    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], height[i])

    water = 0

    for i in range(n):
        water += min(left_max[i], right_max[i]) - height[i]

    return water


height = [0,1,0,2,1,0,1,3,2,1,2,1]

print(trappingRainWater_prefix(height))

#Two pointers 

def trappingRainWater_twoPointers(height):

    left = 0
    right = len(height) - 1

    left_max = 0
    right_max = 0

    water = 0

    while left < right:

        if left_max < right_max:

            left += 1

            left_max = max(left_max, height[left])

            water += left_max - height[left]

        else:

            right -= 1

            right_max = max(right_max, height[right])

            water += right_max - height[right]

    return water


height = [0,1,0,2,1,0,1,3,2,1,2,1]

print(trappingRainWater_twoPointers(height))