#Count Vowels
list= "education"
Output: 5
def countVowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0

    for ch in s.lower():
        if ch in vowels:
            count += 1

    return count

print(countVowels(list))
# Time: O(n)
# Space: O(1)
# Interview Answer

# Traverse the string once. For each character, check whether it is a vowel and increment the count. Since the vowel set contains only 5 characters, the lookup is constant time. Overall complexity is O(n) time and O(1) space.