def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if len(strs) == 0:
        return ""
    if len(strs) == 1:
        return strs[0]
    count = 0
    longestCommonStr = strs[0]
    for i in range(len(longestCommonStr)):
        for item in strs[1:]:
            if longestCommonStr == item[:len(longestCommonStr)]:
                count += 1
        if count == len(strs) - 1:
            return longestCommonStr
        else:
            count = 0
            longestCommonStr = longestCommonStr[:-1]
    return ""


if __name__ == "__main__":
    print(longestCommonPrefix(["flower", "flow", "flight"]))

