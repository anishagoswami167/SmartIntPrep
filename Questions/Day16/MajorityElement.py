 #Majority element
l=[3,2,3]
Output=3

def majorityEle(l):
    d={}
    res=[]
    for i in l:
        d[i]=d.get(i,0)+1
    for k,v in d.items():
        if v>len(l)//2:
            return k
    
print(majorityEle(l))


#(Boyer-Moore Voting Algorithm)
def majorityEle(nums):

    candidate = None
    count = 0

    for num in nums:

        if count == 0:
            candidate = num

        if num == candidate:
            count += 1
        else:
            count -= 1

    return candidate

print(majorityEle([3,2,3]))