def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """

    if str(x) == str(x)[::-1]:
        return True
    return False

if __name__ == "__main__":
    print(isPalindrome(121))
