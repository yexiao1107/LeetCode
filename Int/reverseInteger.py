'''给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21

'''


def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    if x > 0:
        x = int(str(x)[::-1])
    else:
        x = -int(str(-x)[::-1])
    if x > 2 ** 31 - 1 or x < -2 ** 31:
        return 0
    return x


if __name__ == "__main__":
    print(reverse(123))
