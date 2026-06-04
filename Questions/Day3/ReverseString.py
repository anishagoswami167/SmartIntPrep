def reverseString(s):

    res = []

    for i in range(len(s)-1, -1, -1):
        res.append(s[i])

    return "".join(res)

print(reverseString("python"))

#Time: O(n)
#Space: O(n)

s = "python"

print("".join(reversed(s)))

#Time: O(n)
#Space: O(n)


def reverseString(s):
    res = ""

    for i in range(len(s)-1, -1, -1):
        res += s[i]

    return res

print(reverseString("python"))
#Time: O(n²) Because strings are immutable.
#Space: O(n)
