'''
实现函数double Power(double base, int exponent)，求base的exponent次方。
不得使用库函数，同时不需要考虑大数问题。


示例 1:

输入: 2.00000, 10
输出: 1024.00000
示例2:

输入: 2.10000, 3
输出: 9.26100
示例3:

输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25
'''


class Solution:
    def myPow(self, x: float, n: int) -> float:
        '''
        快速幂，二分法思想
        :param x:
        :param n:
        :return:
        '''
        if x == 0: return 0
        if n < 0: x, n = 1 / x, -n
        res = 1
        while n:
            if n & 1:
                res *= x
            x *= x
            n //= 2
        return res
if __name__=="__main__":
    solution = Solution()
    print(solution.myPow(2.1,3))