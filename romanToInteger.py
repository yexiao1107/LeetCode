def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    dict_romantonum = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    temp = s[0]
    sum = dict_romantonum[s[0]]
    for item in s[1:]:
        if dict_romantonum[item] <= dict_romantonum[temp]:
            sum += dict_romantonum[item]
        else:
            sum = sum + dict_romantonum[item] - 2 * dict_romantonum[temp]
        temp = item
    return sum


if __name__ == "__main__":
    print(romanToInt("XXVII"))
