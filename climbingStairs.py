def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 1:
        return 1
    a = 1
    b = 2
    count = 2
    while count < n:
        a, b = b, a + b
        count += 1
    return b

if __name__ == "__main__":
    print(climbStairs(2))