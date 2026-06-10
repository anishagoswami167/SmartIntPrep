#Longest Common Prefix
strs=["flower","flow","flight"]
Output="fl"

def longestPrefix(strs):

    if not strs:
        return ""

    for i in range(len(strs[0])):

        for word in strs:

            if i >= len(word) or word[i] != strs[0][i]:
                return strs[0][:i]

    return strs[0]

print(longestPrefix(strs))


# Approach:
# Use the first string as reference.
# Compare characters at each position across all strings.
# Stop when a mismatch is found and return the prefix.

# Time Complexity:
# O(n × m)

# where:
# n = number of strings
# m = length of shortest string

# Space Complexity:
# O(1)