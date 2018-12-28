def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    if len(s) == "":
        return 0
    wordlist = s.strip().split(" ")
    return len(wordlist[-1])

if __name__ == "__main__":
    print(lengthOfLastWord("Hello World"))
