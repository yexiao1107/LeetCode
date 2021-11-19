'''
大顶堆实现，大顶堆满足arr[i] >= arr[2i+1] && arr[i] >= arr[2i+2]
'''


class BigHeap():
    def __init__(self, array):
        self.array = array
        self.mark = 1
        while self.mark == 1:
            self.build()

    def build(self):
        self.mark = 0
        index = len(self.array) - 1
        for i in range(index):
            if i * 2 + 2 <= index:
                self.tri(i, i * 2 + 1, i * 2 + 2)
            elif i * 2 + 1 <= index:
                if self.array[i] <= self.array[i * 2 + 1]:
                    self.swap(i, i * 2 + 1)
            else:
                break

    def tri(self, head, left, right):
        if self.array[head] < self.array[left]:
            self.swap(head, left)
        if self.array[head] < self.array[right]:
            self.swap(head, right)

    def swap(self, index1, index2):
        self.mark = 1
        self.array[index1], self.array[index2] = self.array[index2], self.array[index1]

    def pop_head(self):
        self.array[0] = self.array[-1]
        res = self.array.pop()
        self.mark = 1
        while self.mark == 1:
            self.build()
        return res

    def push_head(self, value):
        self.array.append(value)
        self.mark = 1
        while self.mark == 1:
            self.build()
