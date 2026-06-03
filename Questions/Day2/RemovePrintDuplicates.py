#Remove and print duplicates using set
li=[1,1,2,3,3,4]

def remDup(li):
    s=set()
    d= set()
    for l in li:
        if l not in s:
            s.add(l)
        else:
            d.add(l)
    return s,d
    
print(remDup(li))

#Only need to give list of unique numbers           
def remDup(li):
    return list(set(li))

print(remDup([1,1,2,3,3,4]))

#⚠️ Note: set() may not preserve order.
def remDup(li):
    seen = set()
    result = []

    for num in li:
        if num not in seen:
            seen.add(num)
            result.append(num)

    return result

print(remDup([1,1,2,3,3,4]))


# Time Complexity: O(n)
# Reason: We traverse the list once, and set operations
# (add, lookup) take O(1) on average.

# Space Complexity: O(n)
# Reason: We use two sets to store unique and duplicate elements.
# In the worst case, they can store up to n elements.