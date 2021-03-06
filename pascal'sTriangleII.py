def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    tri = [[1]]
    for i in range(1, rowIndex + 1):
        tri[0].append(0)
        for j in range(i, 0, -1):
            if j == i:
                tri[0][j] = 1
            else:
                tri[0][j] += tri[0][j - 1]
    return tri[0]


if __name__ == "__main__":
    print(getRow(4))
