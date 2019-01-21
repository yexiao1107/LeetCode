def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    s = ''.join(filter(str.isalnum,s)).lower()
    return s == s[::-1]

if __name__ == "__main__":
    print(isPalindrome("A man, a plan, a canal: Panama"))
