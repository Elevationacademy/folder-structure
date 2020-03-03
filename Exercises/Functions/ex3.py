LONG_STRING = 10


def is_long_string(text):
    return len(text) > LONG_STRING


def judge(str1, str2):
    longest = str1 if len(str1) > len(str2) else str2
    if is_long_string(longest):
        print(longest, "is a long string")
    else:
        print(longest, "is a normal string")


judge("shepherd", "cataclysmic")
judge("horse", "cat")
