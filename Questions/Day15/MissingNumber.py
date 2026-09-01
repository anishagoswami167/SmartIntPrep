#Find missing number
arr= [1,2,4,5]
Output=3
def missingNumber(arr):
    for i in range(len(arr)-1):
        if arr[i+1]-arr[i]!=1:
            return arr[i]+1
print(missingNumber(arr))



def missingNumber(arr,n):

    xor1 = 0
    xor2 = 0

    for i in range(1,n+1):
        xor1 ^= i

    for num in arr:
        xor2 ^= num

    return xor1 ^ xor2