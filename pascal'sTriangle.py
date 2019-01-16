def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    ret = []
    for i in range(numRows):
        ret.append([1])
        for j in range(1, i + 1):
            if j == i:
                ret[i].append(1)
            else:
                ret[i].append(ret[i-1][j] + ret[i-1][j-1])
    return ret

if __name__ == "__main__":
    res = generate(5)
    for item in res:
        print(item)