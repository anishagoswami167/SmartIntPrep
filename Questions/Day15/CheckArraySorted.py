#Check if array is sorted
arr=[1,2,3,4]
Output=True

def checkArraySorted(arr):
 
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
       
    return True
print(checkArraySorted(arr)) 
