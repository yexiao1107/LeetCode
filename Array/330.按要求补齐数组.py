'''
给定一个已排序的正整数数组 nums，和一个正整数n 。
从[1, n]区间内选取任意个数字补充到nums中，
使得[1, n]区间内的任何数字都可以用nums中某几个数字的和来表示。
请输出满足上述要求的最少需要补充的数字个数。

示例1:

输入: nums = [1,3], n = 6
输出: 1
解释:
根据 nums里现有的组合[1], [3], [1,3]，可以得出1, 3, 4。
现在如果我们将2添加到nums 中，组合变为: [1], [2], [3], [1,3], [2,3], [1,2,3]。
其和可以表示数字1, 2, 3, 4, 5, 6，能够覆盖[1, 6]区间里所有的数。
所以我们最少需要添加一个数字。
示例 2:

输入: nums = [1,5,10], n = 20
输出: 2
解释: 我们需要添加[2, 4]。
'''


class Solution:
    def minPatches(self, nums, n: int) -> int:
        '''
        补齐数组特点：
        假设数组 arrarr 添加一个元素即可覆盖 [1, n)[1,n) 内所有数字，那么添加的数字 mm 一定满足m <= n。
        假设数组 arrarr 可以覆盖 [1, n)[1,n) 的所有数字，则给 arrarr 内加元素 mm ：
        若m <= n，新数组可以覆盖[1, m + n) = [1, n) ∪ [m, m + n)内所有数字；
        贪心法则： 对于一个覆盖 [1, n)[1,n) 的数组 arrarr 来说，添加数字 nn 连续扩容范围最大（扩容至 [1, 2n)[1,2n) ）。
        思路： 设置一个初始范围 [1, 1)[1,1) ，通过不断确认并扩大数组可以覆盖的范围，最终计算出最少需要加入的数字。
        当i < len(nums)且nums[i] <= add时：不需要加入新数字，循环确认并更新数组可以覆盖的范围[1, add + nums[i])，直到找到大于确认范围 addadd 的 nums[i]nums[i] 或索引越界。
        否则：无法根据现有数字构建更大的连续范围，，因此需要使用贪心策略向数组加入数字 addadd ，将数组从覆盖 [1, add)[1,add) 扩容至可覆盖 [1, 2add)[1,2add) 。
        直到确认的范围add > n，说明此时已经覆盖 [1, n][1,n] ，退出迭代并返回。
        :param nums:
        :param n:
        :return:
        '''
        add, i, count = 1, 0, 0
        while add <= n:
            if i < len(nums) and nums[i] <= add:
                add += nums[i]  # from [1, add] to [1, add + nums[i]]
                i += 1
            else:
                add += add  # from [1, add] to [1, 2add]
                count += 1
        return count


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 5, 10]
    n = 20
    solution.minPatches(nums, n)
