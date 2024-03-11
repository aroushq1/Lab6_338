import timeit
import random

class BinaryTreeNode:
    def __init__(self, value, parent=None, left=None, right=None):
        self.parent = parent
        self.value = value
        self.left = left
        self.right = right

    @staticmethod
    def insert(value, root=None):
        current_node = root
        parent_node = None

        while current_node is not None:
            parent_node = current_node
            if value <= current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right

        if root is None:
            root = BinaryTreeNode(value)
        elif value <= parent_node.value:
            parent_node.left = BinaryTreeNode(value, parent_node)
        else:
            parent_node.right = BinaryTreeNode(value, parent_node)
        return root

    @staticmethod
    def iterative_search(value, root):
        current_node = root
        while current_node is not None and current_node.value != value:
            if value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return current_node

def shuffle_list(input_list):
    random.shuffle(input_list)

def measure_search_performance(shuffled_list, root):
    search_times = []
    for value in shuffled_list:
        search_time = timeit.timeit(lambda: BinaryTreeNode.iterative_search(value, root), number=10) / 10
        search_times.append(search_time)
    avg_search_time = sum(search_times) / len(search_times)
    total_search_time = sum(search_times)
    return avg_search_time, total_search_time

# Generate sorted list
sorted_list = list(range(10000))

# Build binary search tree
root_node = None
for value in sorted_list:
    root_node = BinaryTreeNode.insert(value, root_node)

# Measure search performance
avg_search_time_before_shuffling, total_search_time_before_shuffling = measure_search_performance(sorted_list, root_node)

print("Average search time before shuffling:", avg_search_time_before_shuffling)
print("Total search time before shuffling:", total_search_time_before_shuffling)

# Shuffle the list
shuffled_list = sorted_list[:]
shuffle_list(shuffled_list)

# Measure search performance
avg_search_time_after_shuffling, total_search_time_after_shuffling = measure_search_performance(shuffled_list, root_node)

print("Average search time after shuffling:", avg_search_time_after_shuffling)
print("Total search time after shuffling:", total_search_time_after_shuffling)

"""
After implementing binary search on both sorted and randomly shuffled lists, 
there's hardly any difference in the total and average times. This similarity 
is mainly because the lists are relatively small. However, as the size of the 
lists increases, a significant decrease in time becomes apparent for the sorted 
list compared to the shuffled one. This difference stems from the superior time 
complexity of the sorted list, which is O(log n), in contrast to the O(n) time 
complexity of the shuffled list.
"""