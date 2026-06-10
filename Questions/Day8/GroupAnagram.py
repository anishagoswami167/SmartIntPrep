#Given an array of strings, group all anagrams together.
strs = ["eat","tea","tan","ate","nat","bat"]
# Output
# [
#     ["eat","tea","ate"],
#     ["tan","nat"],
#     ["bat"]
# ]


#I use a HashMap where the key is the sorted version of each word. Since all anagrams produce the same sorted string, they get stored under the same key. Finally, I return all the grouped values from the dictionary.
def groupAnagram(strs):
    d={}
    for s in strs:
        key = "".join(sorted(s))
        if key not in d:
            d[key]=[]
        d[key].append(s)
    return list(d.values())
        
print(groupAnagram(strs))

#TimeComplexity
# Let:
# n = number of words
# k = average length of each word
# Sorting one word:
# O(k log k)
# For n words:
# O(n * k log k)

# Space Complexity
# Dictionary stores all words:
# O(n * k)


def groupAnagram(strs):

    d = {}

    for s in strs:

        key = "".join(sorted(s))

        d.setdefault(key, []).append(s)

    return list(d.values())


#What does setdefault() do?
# d.setdefault(key, [])
#If key doesn't exist, create it with an empty list.
#If it already exists, return the existing list.