'''给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例1:

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
    INT_MAX = pow(2, 31) - 1
    INT_MIN = - pow(2, 31)
    rev = 0
    while x != 0:
        if x > 0:
            pop = x % 10
            x = x // 10
        else:
            pop = x % -10
            x = -(x // -10)
        if rev > INT_MAX / 10 or (rev == INT_MAX // 10 and pop > 7):
            return 0
        if rev < INT_MIN / 10 or (rev == INT_MIN // 10 and pop < -8):
            return 0
        rev = rev * 10 + pop
    return rev


if __name__ == "__main__":
    print(reverse(-123))
