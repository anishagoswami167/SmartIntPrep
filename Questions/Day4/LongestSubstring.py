#Longest Substring Without Repeating Characters
s = "abcdabcbb"
# Output:3


# Brute Force Approach
# Thinking Process

# Generate every possible substring.

# For every substring:

# Check if all characters are unique.
# If unique:
# Calculate its length.
# Update maximum length.

# Finally return maximum length.

def longestSubstringBrute(s):

    maxlen = 0

    for i in range(len(s)):

        for j in range(i, len(s)):

            sub = s[i:j+1]

            if len(sub) == len(set(sub)):
                maxlen = max(maxlen, len(sub))

    return maxlen

print(longestSubstringBrute("abcabcbb"))

def lonSubstring(s):
    seen=set()
    j=0
    maxcount=0
    for i in range(len(s)):
        while s[i] in seen:
            seen.remove(s[i])
            j+=1
        seen.add(s[i])
        maxcount=max(maxcount,i-j+1)
        
            
    return maxcount
print(lonSubstring(s))


# Got it 😄. You mean:

# > **How would I explain Brute Force → Sliding Window optimization for Longest Substring Without Repeating Characters in an interview?**

# This is a very common interview discussion.

# ---

# # Problem

# ```python id="s6sqe5"
# s = "abcabcbb"
# ```

# Output:

# ```python id="t6rq1l"
# 3
# ```

# Because:

# ```text id="gsrlu6"
# "abc"
# ```

# is the longest substring without repeating characters.

# ---

# # Step 1: Brute Force Thinking

# ### My first idea

# Generate every possible substring.

# For each substring:

# ```text id="dc0fqa"
# Check whether all characters are unique.
# ```

# If yes:

# ```text id="wz45fy"
# Update maximum length.
# ```

# ---

# ## Example

# ```python id="l8n01u"
# s = "abcabcbb"
# ```

# Substrings:

# ```text id="0zz8tw"
# a
# ab
# abc
# abca
# abcab
# ...
# ```

# For each substring:

# ```python id="55g98x"
# len(sub) == len(set(sub))
# ```

# to check uniqueness.

# ---

# ### Brute Force Code

# ```python id="mgl4p0"
# def longestSubstringBrute(s):

#     maxlen = 0

#     for i in range(len(s)):
#         for j in range(i, len(s)):

#             sub = s[i:j+1]

#             if len(sub) == len(set(sub)):
#                 maxlen = max(maxlen, len(sub))

#     return maxlen
# ```

# ---

# # Time Complexity

# Generate substrings:

# ```text id="pq5vgq"
# O(n²)
# ```

# Check uniqueness:

# ```text id="78quzn"
# O(n)
# ```

# Total:

# ```text id="ynrzxp"
# O(n³)
# ```

# ---

# # Problem With Brute Force

# Let's observe.

# ```python id="od5r11"
# s = "abcabcbb"
# ```

# Generated substrings:

# ```text id="xgk8k9"
# abc
# abca
# abcab
# abcabc
# ```

# Notice:

# ```text id="7rt5fu"
# abc
# ```

# is being checked again and again inside larger substrings.

# We're doing lots of repeated work.

# ---

# # Key Observation

# Suppose current valid substring is:

# ```text id="3l6v98"
# abc
# ```

# Next character:

# ```text id="lw2r7m"
# a
# ```

# Now:

# ```text id="v2r4zq"
# abca
# ```

# has duplicate `'a'`.

# Do we need to restart from scratch?

# No.

# We can simply remove characters from the left until the duplicate disappears.

# ---

# # Sliding Window Idea

# Maintain a window:

# ```text id="n7imz1"
# [left -------- right]
# ```

# containing only unique characters.

# Also maintain a set.

# ---

# ## Example

# Start:

# ```text id="ygbg72"
# a
# ```

# Window:

# ```text id="1kqkzn"
# [a]
# ```

# Set:

# ```python id="2b6ul0"
# {'a'}
# ```

# Length:

# ```python id="fovszr"
# 1
# ```

# ---

# Expand:

# ```text id="z7ajoz"
# ab
# ```

# Set:

# ```python id="qfhd0r"
# {'a','b'}
# ```

# Length:

# ```python id="nb82kh"
# 2
# ```

# ---

# Expand:

# ```text id="6my6fe"
# abc
# ```

# Set:

# ```python id="afscm4"
# {'a','b','c'}
# ```

# Length:

# ```python id="v32j8s"
# 3
# ```

# ---

# Next character:

# ```text id="v7mrkw"
# a
# ```

# Duplicate found.

# Current window:

# ```text id="a2xqvh"
# abc
# ^
# left
# ```

# Remove leftmost:

# ```python id="jlwm4f"
# remove('a')
# ```

# Window becomes:

# ```text id="xwckq2"
# bc
# ```

# Now add new `'a'`

# Window:

# ```text id="bqppwq"
# bca
# ```

# Still unique.

# No restart needed.

# ---

# # Sliding Window Code

# ```python id="iql5is"
# def longestSubstring(s):

#     seen = set()

#     left = 0
#     maxlen = 0

#     for right in range(len(s)):

#         while s[right] in seen:

#             seen.remove(s[left])
#             left += 1

#         seen.add(s[right])

#         maxlen = max(maxlen, right-left+1)

#     return maxlen
# ```

# ---

# # Interview Explanation

# A strong answer:

# ```text id="ghy2tw"
# My brute force approach is to generate every substring and check whether all characters are unique.

# This takes O(n³) time because there are O(n²) substrings and checking uniqueness takes O(n).

# To optimize, I observe that adjacent substrings share most of their characters. Instead of rebuilding every substring, I maintain a sliding window containing unique characters.

# Whenever a duplicate character appears, I shrink the window from the left until the duplicate is removed. This allows me to process each character at most twice.

# Thus the time complexity becomes O(n).
# ```

# ---

# # Complexity Comparison

# | Approach       | Time  | Space |
# | -------------- | ----- | ----- |
# | Brute Force    | O(n³) | O(n)  |
# | Sliding Window | O(n)  | O(n)  |

# ---

# ### The Most Important Insight

# For this problem, Sliding Window is not about:

# ```text id="80g0fj"
# Removing one element and adding one element
# ```

# (like Maximum Sum Subarray).

# Instead it's about:

# ```text id="z24z5v"
# Expand right pointer

# If duplicate found:
#     shrink left pointer

# Maintain a valid window
# ```

# This is called **Variable Size Sliding Window**, whereas the maximum-sum-of-size-k problem is **Fixed Size Sliding Window**.

# That's the key difference interviewers expect you to understand. 🚀
