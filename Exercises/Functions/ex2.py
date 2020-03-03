def longest_string(str1, str2):
    if len(str1) > len(str2):
        return str1
    elif len(str2) > len(str1):
        return str2
    return "same length"


print(longest_string("abc", "ab"))
print(longest_string("ab", "abc"))
print(longest_string("abc", "abc"))