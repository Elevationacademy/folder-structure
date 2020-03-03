def longest_string(str1, str2):
    return str1 if len(str1) > len(str2) else str2


print(longest_string("abc", "ab"))
print(longest_string("ab", "abc"))
