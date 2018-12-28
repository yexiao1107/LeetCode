def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    if len(s) == 0:
        return True
    dict_par = {"(": ")", "[": "]", "{": "}"}
    temp = []
    for item in s:
        if item in dict_par:
            temp.append(item)
        else:
            if len(temp) == 0:
                return False
            elif item == dict_par[temp[-1]]:
                temp.pop()
            else:
                return False
    if len(temp) == 0:
        return True
    return False


if __name__ == "__main__":
    print(isValid("[]"))
