def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if needle=="":
        return 0
    for i in range(len(haystack)):
        temp = haystack[i:][:len(needle)]
        if needle == temp:
            return i
    return -1

if __name__ =="__main__":
    print(strStr("hello","ll"))