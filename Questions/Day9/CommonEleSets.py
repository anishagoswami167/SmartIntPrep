#Find Common Elements in Two Arrays
nums1 = [1,2,2,1]
nums2 = [2,2]
Output=[2]

def commonEle(nums1,nums2):
    s1=set()
    s2=set()
    for n in nums1:
        if n not in s1:
            s1.add(n)
    for n in nums2:
        if n not in s2:
            s2.add(n)
            
    return list(s1&s2)

print(commonEle(nums1,nums2))

# Time Complexity
# Creating sets: O(n + m)
#Intersection: O(min(n,m))
#Overall: O(n + m)

#Space Complexity

#Two sets: O(n + m)

#BruteForce
def commonEle(nums1, nums2):
    res = []

    for n1 in nums1:
        for n2 in nums2:

            if n1 == n2 and n1 not in res:
                res.append(n1)

    return res
#Time Complexity: O(n)*O(m)

#Space Complexity: O(1)
