'''
算法步骤

将第一待排序序列第一个元素看做一个有序序列，把第二个元素到最后一个元素当成是未排序序列。

从头到尾依次扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置。（如果待插入的元素与有序序列中的某个元素相等，则将待插入元素插入到相等元素的后面。）
时间复杂度O(n^2), 空间复杂度O(1), 稳定
'''


def insertionSort(arr):
    for i in range(len(arr)):
        pre_index = i - 1
        cur = arr[i]
        while pre_index >= 0 and arr[pre_index] > cur:
            arr[pre_index + 1] = arr[pre_index]
            pre_index -= 1
        arr[pre_index + 1] = cur
    return arr


if __name__ == "__main__":
    arr = [4, 3, 2, 1]
    print(insertionSort(arr))
