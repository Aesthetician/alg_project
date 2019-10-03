def swap(a, i, j):
  a[i], a[j] = a[j], a[i]
  #print(a[i])
  #print(a[j])
  
def sift_down(a, n, max):
  while True:
    biggest = n
    c1 = 2*n + 1
    c2 = c1 + 1
    for c in [c1, c2]:
      if c < max and a[c][0] > a[biggest][0]:
        biggest = c
    if biggest == n:
      return
    swap(a, n, biggest)
    n = biggest

def heapify(a):
  i = len(a) // 2 - 1
  max = len(a)
  while i >= 0:
    sift_down(a, i, max)
    i -= 1

def heapsort(a):
  heapify(a)
  j = len(a) - 1
  while j > 0:
    swap(a, 0, j)
    sift_down(a, 0, j)
    j -= 1

if __name__ == "__main__":
    a = [12, 11, 10, 9, 8, 7, 1, 2, 3, 4, 5, 6]
    b = [[2, 0, 1], [1, 0, 2], [5, 0, 3], [2, 1, 0], [2, 1, 2], [3, 1, 3], [1, 2, 0], [2, 2, 1], [1, 2, 4], [3, 2, 3], [5, 3, 0], [3, 3, 1], [3, 3, 2], [1, 3, 4], [5, 3, 5], [1, 4, 2], [1, 4, 3], [1, 4, 5], [5, 5, 3], [1, 5, 4]]
    heapsort(a)
    print(a)
    heapsort(b)
    print(b)
    