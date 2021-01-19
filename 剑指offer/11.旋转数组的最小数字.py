'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  

示例 1：

输入：[3,4,5,1,2]
输出：1
示例 2：

输入：[2,2,2,0,1]
输出：0
'''


class Solution:
    def minArray(self, numbers) -> int:
        for i in range(len(numbers)):
            if numbers[0] >= numbers[-1]:
                numbers.append(numbers.pop(0))
        return numbers[0]

    def minArray2(self, numbers) -> int:
        '''
        二分查找
        m = (i+j)/2
        当num[m]>num[j],旋转点在[m+1,j]
        num[m]<num[j],旋转点在[i,m]
        num[m]=num[j],无法判断旋转点的位置，故只能将j-1
        :param numbers:
        :return:
        '''
        i, j = 0, len(numbers) - 1
        while i < j:
            m = (i + j) // 2
            if numbers[m] > numbers[j]:
                i = m + 1
            elif numbers[m] < numbers[j]:
                j = m
            else:
                j -= 1
        return numbers[i]


if __name__ == "__main__":
    solution = Solution()
    print(solution.minArray([3, 4, 5, 1, 2]))
