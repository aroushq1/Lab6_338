import heapq
import random
import timeit

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class ListPriorityQueue:
    def __init__(self):
        self.head = None
    
    def enqueue(self, value):
        new_node = ListNode(value)
        if not self.head or value <= self.head.value:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.value < value:
                current = current.next
            new_node.next = current.next
            current.next = new_node
    
    def dequeue(self):
        if not self.head:
            return None
        else:
            value = self.head.value
            self.head = self.head.next
            return value

class HeapPriorityQueue:
    def __init__(self):
        self.heap = []
    
    def enqueue(self, value):
        heapq.heappush(self.heap, value)
    
    def dequeue(self):
        if self.heap:
            return heapq.heappop(self.heap)
        else:
            return None

def generate_random_tasks():
    tasks = []
    for _ in range(1000):
        if random.random() < 0.7:
            tasks.append(('enqueue', random.randint(1, 1000)))
        else:
            tasks.append(('dequeue', None))
    return tasks

tasks = generate_random_tasks()

def measure_execution_time(queue_class):
    queue = queue_class()
    start_time = timeit.default_timer()
    for task in tasks:
        if task[0] == 'enqueue':
            queue.enqueue(task[1])
        else:
            queue.dequeue()
    end_time = timeit.default_timer()
    return end_time - start_time

list_time = measure_execution_time(ListPriorityQueue)
heap_time = measure_execution_time(HeapPriorityQueue)

print("ListPriorityQueue execution time:", list_time)
print("HeapPriorityQueue execution time:", heap_time)
print("Average time per task for ListPriorityQueue:", list_time / len(tasks))
print("Average time per task for HeapPriorityQueue:", heap_time / len(tasks))


# Question #4:
# The HeapPriorityQueue implementation is expected to be faster than the ListPriorityQueue implementation
# because it is based on a heap, which contains a better time complexity for the enqueue and dequeue operations compared to
# that of the ListPriorityQueue, which uses a linked list-based approach.
# Furthermore the HeapPriorityQueue implementation proves to be more efficient with regards To maintaining priority queues,
# especially when dealing with large datasets. This efficency originates from the properities of the heap data structure
# in which insertion and deletion are performed efficiently while simultaneously maintaining the heap property. 
# Thus the HeapPriorityQueue outperforms ListPriorityQueue in terms of execution time.

#the above code was generated using chatGPT but was modified to give accurate results
