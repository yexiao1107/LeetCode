'''
给定一个非负整数N，找出小于或等于N的最大的整数，同时这个整数需要满足其各个位数上的数字是单调递增。

（当且仅当每个相邻位数上的数字x和y满足x <= y时，我们称这个整数是单调递增的。）

示例 1:

输入: N = 10
输出: 9
示例 2:

输入: N = 1234
输出: 1234
示例 3:

输入: N = 332
输出: 299
说明: N是在[0, 10^9]范围内的一个整数。
'''


class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        res = list(str(N))
        length = len(res)

        for i in range(length - 1, 0, -1):
            if res[i] < res[i - 1]:
                res[i - 1] = str(int(res[i - 1]) - 1)
                res[i:] = ['9'] * (length - i)
        return int(''.join(res))


if __name__ == "__main__":
    num = 332
    solution = Solution()
    print(solution.monotoneIncreasingDigits(num))
