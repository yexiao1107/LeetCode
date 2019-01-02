def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """
    if x == 0:
        return x
    low = 1
    high = x // 2 + 1
    while low <= high:
        counter = (low + high) // 2
        if counter ** 2 == x:
            return counter
        elif counter ** 2 < x:
            low += 1
        else:
            high -= 1
    return high

if __name__ == "__main__":
    print(mySqrt(2147395599))