def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    if len(a) < len(b):
        a, b = b, a

    a = "0" + a
    for i in range(0, (len(a) - len(b))):
        b = "0" + b

    carry = 0;
    result = "";

    for i in range(len(a) - 1, -1, -1):
        temp = int(a[i]) + int(b[i]) + carry
        carry = temp // 2
        result = str(temp % 2) + result

    if result[0] == "0":
        return result[1:]
    else:
        return result

if __name__ == "__main__":
    print(addBinary("111","011"))