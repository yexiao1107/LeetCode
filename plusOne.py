def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    flag = 1
    for i in range(len(digits)-1,-1,-1):
        if digits[i] + flag == 10:
            digits[i] = 0
            flag = 1
        else:
            digits[i] = digits[i] + flag
            flag = 0
    if flag == 1:
        digits.insert(0,1)
    return digits

if __name__ == "__main__":
    print(plusOne([9,9,9]))