class min_heap:
    '''array[0] is unused'''
    def __init__(self):
        self.size = 0
        self.array = [0]

    def isEmpty(self):
        if self.size == 0:
            res = 1
        else:
            res = 0            
        return res

    def decrease_key(self, i, k):
        if k > self.array[i]:
            print('given key is larger than current key')
        self.array[i] = k
        self.heapify_up(i)

    def insert(self, node):
        self.array.append(node)
        self.size += 1
        self.heapify_up(self.size)

    def delete(self, idx):
        self.array[idx] = self.array[self.size]
        self.size -= 1
        self.array.pop()
        self.heapify_down(idx)
        return 1

    def get_min(self):
        return self.array[1]

    def extract_min(self):
        res = self.array[1]
        self.array[1] = self.array[self.size]
        self.size -= 1
        self.array.pop()
        self.heapify_down(1)
        return res

    def build_heap(self, a_list):
        self.size = len(a_list)
        self.array = [0] + a_list[:]
        i = len(a_list) // 2
        while i > 0:
            self.heapify_down(i)
            i = i - 1
        return 1

    def swap(self, a, b):
        tmp = b
        b = a
        a = tmp
        return a, b

    '''
    def heapify_up(self, idx):
        if self.array[self.parent(idx)] < self.array[idx]:
            self.array[self.parent(idx)], self.array[idx] = self.swap(self.array[self.parent(idx)], self.array[idx])
            self.heapify_up(self.parent(idx))
        else:
            return
    '''

    def heapify_up(self, idx):
        i = idx
        while i > 1 and self.array[self.parent(i)] < self.array[i]:
            self.array[self.parent(i)], self.array[i] = self.swap(self.array[self.parent(i)], self.array[i])
            i = self.parent(i)
        return

    def heapify_down(self, idx):
        i = idx
        while i < self.size:
            l = self.child_left(i)
            r = self.child_right(i)
            if l <= self.size and self.array[l] < self.array[i]:
                idx_min = l
            else:
                idx_min = i
                
            if r <= self.size and self.array[r] < self.array[idx_min]:
                idx_min = r
            if idx_min == i:
                break
            else:
                self.array[i], self.array[idx_min] = self.swap(self.array[i], self.array[idx_min])
                i = idx_min
        return 1

    def parent(self, idx):
        return int(idx / 2)

    def child_left(self, idx):
        return 2 * idx

    def child_right(self, idx):
        return 2 * idx + 1


if __name__ == "__main__":
    # test code
    bh = min_heap()
    bh.build_heap([9,5,6,2,3])
    print(bh.extract_min())
    print(bh.extract_min())
    print(bh.extract_min())
    print(bh.extract_min())
    print(bh.extract_min())




