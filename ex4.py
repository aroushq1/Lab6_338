class MinHeap:
    def __init__(self):
        self.heap = []

    def heapify(self, arr):
        self.heap = arr
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            self._min_heapify(i)

    def enqueue(self, item):
        self.heap.append(item)
        self._up_heapify(len(self.heap) - 1)

    def dequeue(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        min_item = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._min_heapify(0)
        return min_item

    def _min_heapify(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = i
        if left < len(self.heap) and self.heap[left] < self.heap[i]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self._min_heapify(smallest)

    def _up_heapify(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[i] < self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break


import unittest
import random

class TestMinHeap(unittest.TestCase):
    def test_sorted_heap(self):
        heap = MinHeap()
        input_arr = [1, 2, 3, 4, 5]
        heap.heapify(input_arr)
        self.assertListEqual(heap.heap, [1, 2, 3, 4, 5])

    def test_empty_heap(self):
        heap = MinHeap()
        input_arr = []
        heap.heapify(input_arr)
        self.assertListEqual(heap.heap, [])

    def test_random_heap(self):
        heap = MinHeap()
        input_arr = random.sample(range(1, 101), 100)
        heap.heapify(input_arr)
        self.assertListEqual(heap.heap, sorted(input_arr))

if __name__ == '__main__':
    unittest.main()
