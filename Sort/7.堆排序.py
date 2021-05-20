'''
算法步骤

创建一个堆 H[0……n-1]；

把堆首（最大值）和堆尾互换；

把堆的尺寸缩小 1，并调用 shift_down(0)，目的是把新的数组顶端数据调整到相应位置；

重复步骤 2，直到堆的尺寸为 1。
'''


# 调整父节点 与孩子大小， 制作大顶堆
def adjust_heap(data, par_node, high):
    new_par_node = par_node
    j = 2 * par_node + 1  # 取根节点的左孩子， 如果只有一个孩子 high就是左孩子，如果有两个孩子 high 就是右孩子

    while j <= high:  # 如果 j = high 说明没有右孩子，high就是左孩子
        if j < high and data[j] < data[j + 1]:  # 如果这儿不判断 j < high 可能超出索引
            # 一个根节点下，如果有两个孩子，将 j  指向值大的那个孩子
            j += 1
        if data[j] > data[new_par_node]:  # 如果子节点值大于父节点，就互相交换
            data[new_par_node], data[j] = data[j], data[new_par_node]
            new_par_node = j  # 将当前节点，作为父节点，查找他的子树
            j = j * 2 + 1

        else:
            # 因为调整是从上到下，所以下面的所有子树肯定是排序好了的，
            # 如果调整的父节点依然比下面最大的子节点大，就直接打断循环，堆已经调整好了的
            break


# 索引计算: 0 -->1 --->....
#    父节点 i   左子节点：2i +1  右子节点：2i +2  注意：当用长度表示最后一个叶子节点时 记得 -1
#    即 2i + 1 = length - 1 或者 2i + 2 = length - 1
#    2i+1 + 1 = length 或 2i+2 + 1 = length
#    2(i+1)=length 或 2(i+1）+1 = length
#    设j = i+1  则左子节点(偶数)：2j = length 和 右子节点(基数)：2j+1 = length
#    2j//2 = j == (2j+1)//2 这两个的整除是一样的，所以使用length//2 = j 然后 i + 1 = j
#    i = j-1  = length//2 -1  #注意左子节点:2i+1 //2 =i  而右子节点：(2i+2)//2 = i+1

# 从第一个非叶子节点(即最后一个父节点)开始，即 list_.length//2 -1（len(list_)//2 - 1）

# 开始循环到 root 索引为：0 的第一个根节点， 将所有的根-叶子 调整好，成为一个 大顶堆
def heap_sort(lst):
    """
    根据列表长度，找到最后一个非叶子节点，开始循化到 root 根节点，制作 大顶堆
    :param lst: 将列表传入
    :return:
    """
    length = len(lst)
    last = length - 1  # 最后一个元素的 索引
    last_par_node = length // 2 - 1

    while last_par_node >= 0:
        adjust_heap(lst, last_par_node, length - 1)
        last_par_node -= 1  # 每调整好一个节点，从后往前移动一个节点

    # return lst

    while last > 0:
        # swap(lst, 0, last)
        lst[0], lst[last] = lst[last], lst[0]
        # 调整堆让 adjust 处理，最后已经排好序的数，就不处理了
        adjust_heap(lst, 0, last - 1)
        last -= 1

    return lst  # 将列表返回


##第二种方式
def buildMaxHeap(arr):
    import math
    for i in range(math.floor(len(arr) / 2), -1, -1):
        heapify(arr, i)


def heapify(arr, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < arrLen and arr[left] > arr[largest]:
        largest = left
    if right < arrLen and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        swap(arr, i, largest)
        heapify(arr, largest)


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def heapSort(arr):
    global arrLen
    arrLen = len(arr)
    buildMaxHeap(arr)
    for i in range(len(arr) - 1, 0, -1):
        swap(arr, 0, i)
        arrLen -= 1
        heapify(arr, 0)
    return arr


if __name__ == '__main__':
    list_ = [4, 7, 0, 9, 1, 5, 3, 3, 2, 6]
    heap_sort(list_)
    print(list_)
