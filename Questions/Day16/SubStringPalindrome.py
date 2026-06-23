 #Longest palindrome substring
strs="babad"
Output="bab"

def longestPalindrome(s):

    res = ""

    for i in range(len(s)):

        # Odd length

        l = r = i

        while l >= 0 and r < len(s) and s[l] == s[r]:

            if r-l+1 > len(res):
                res = s[l:r+1]

            l -= 1
            r += 1

        # Even length

        l = i
        r = i+1

        while l >= 0 and r < len(s) and s[l] == s[r]:

            if r-l+1 > len(res):
                res = s[l:r+1]

            l -= 1
            r += 1

    return res

print(longestPalindrome("babad"))

#Interview Explanation

#Every palindrome has a center. I treat each index as a possible center and expand outward while the characters on both sides match. 
# I do this for both odd-length and even-length palindromes and keep track of the longest one found.
#TimeComplexity: O(n*n)
#SpaceComplexity: O(1)
