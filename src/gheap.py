import math 

MAXVAL = math.inf

class min_gheap:
    '''array[0] is unused, array[i] = vid'''
    def __init__(self, capacity=5000):
        self.capacity = capacity
        self.size = 0
        self.array = [0] # main heap array, array[i] = vid
        self.values = [MAXVAL] * self.capacity # values[id] = val
        self.heap_idxs = [0] * self.capacity # heap_idxs[vid] = i

    def isEmpty(self):
        if self.size == 0:
            res = 1
        else:
            res = 0            
        return res

    def vid2hidx(self, vid):
        return self.heap_idxs[vid]

    def vid2value(self, vid):
        res = self.values[vid]
        return res

    def set_value(self, vid, val):
        self.values[vid] = val

    def set_hidx(self, vid, idx):
        self.heap_idxs[vid] = idx

    def decrease_key(self, vid, k): #i: heap array index
        if k > self.vid2value(vid):
            print('given key is larger than current key')
        self.set_value(vid, k)
        self.heapify_up(self.vid2hidx(vid))

    def insert(self, vid, val):
        self.array.append(vid)
        self.size += 1
        self.set_hidx(vid, self.size)
        self.set_value(vid, val)
        self.heapify_up(self.vid2hidx(vid))

    def delete(self, idx):
        #self.array[idx] = self.array[self.size]
        #self.size -= 1
        #self.array.pop()
        #self.heapify_down(idx)
        return 1
    
    def get_min(self):
        vid = self.array[1]
        val = self.vid2value(vid)
        return vid, val 

    def extract_min(self):
        if self.size ==0:
            print('heap is empty and can not ne extracted!')
            return
        else:
            vid, val = self.get_min() 
            self.set_value(vid, MAXVAL) #reset vid's value to MAX
            self.set_hidx(vid, 0) #reset vid's hidx
            self.array[1] = self.array[self.size]
            self.set_hidx(self.array[1], 1)  
            self.size -= 1
            self.array.pop()
            self.heapify_down(1)
            return vid, val

    def build_heap(self, a_list, val_list):
        '''a_list: a list of vid; val_list: a list of vid's value '''
        list_size = len(a_list)
        self.size = list_size
        self.array = [0] + a_list[:]
        #print(self.array)
        [self.set_value(a_list[i], val_list[i]) for i in range(0, list_size)]
        [self.set_hidx(self.array[i], i) for i in range(1, list_size+1)]
        #print(self.heap_idxs)
        i = list_size // 2
        while i > 0:
            self.heapify_down(i)
            i = i - 1
        return 1

    def swap(self, aidx, bidx):
        self.set_hidx(self.array[aidx], bidx)
        self.set_hidx(self.array[bidx], aidx)
        tmp = self.array[bidx]
        self.array[bidx] = self.array[aidx]
        self.array[aidx] = tmp

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
        while i > 1 and self.vid2value(self.array[self.parent(i)]) < self.vid2value(self.array[i]):
            self.swap(i, self.parent(i))
            i = self.parent(i)
        return

    def heapify_down(self, idx):
        i = idx
        while i < self.size:
            l = self.child_left(i)
            r = self.child_right(i)
            if l <= self.size and self.vid2value(self.array[l]) < self.vid2value(self.array[i]):
                idx_min = l
            else:
                idx_min = i
                
            if r <= self.size and self.vid2value(self.array[r]) < self.vid2value(self.array[idx_min]):
                idx_min = r
            if idx_min == i:
                break
            else:
                self.swap(i, idx_min)
                i = idx_min
        return 1

    def parent(self, idx):
        return int(idx / 2)

    def child_left(self, idx):
        return 2 * idx

    def child_right(self, idx):
        return 2 * idx + 1

    def show_arrarys(self):
        print(self.array)
        print(self.values)
        print(self.heap_idxs)


if __name__ == "__main__":
    # test code
    bh = min_gheap(10)
    bh.build_heap([1,2,3,4,5], [5, 9, 2, 6, 3])
    bh.show_arrarys()
    for i in range(0,bh.size):
        print(bh.extract_min())

    bh = min_gheap(15)
    bh.build_heap([11,2,8,4,10,5,14, 0], [5, 9, 2, 6, 3,20,1, 3])
    bh.show_arrarys()
    for i in range(0,bh.size):
        print(bh.extract_min())
    