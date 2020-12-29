"""
Check if two strings could become same if add/remove/modify at most one character.
"""


def solution(str1, str2):
    # mistake1: forgot to add key
    # mistake2: bad result in case of strings with same length
    # str1, str2 = min(str1, str2), max(str1, str2)
    if abs(len(str2) - len(str1)) > 1:
        return False
    i, j = 0, 0
    while i < len(str1) and j < len(str2):
        if str1[i] != str2[j]:
            # print("{}, {}".format(str1[i:], str2[j:]))
            is_substituted = str1[i + 1:] == str2[j + 1:]
            # mistake: forgot to add string slice
            # s_substituted = str1[i + 1] == str2[j + 1]
            if is_substituted:
                return True

            str1, str2 = min(str1, str2, key=len), max(str1, str2, key=len)
            return str1[i:] == str2[j + 1:]
        # print("{} == {}".format(str1[i], str2[j]))
        i += 1
        j += 1
    return True
