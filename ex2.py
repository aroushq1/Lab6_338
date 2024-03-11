class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root_node = None

    def insert(self, value):
        if not self.root_node:
            self.root_node = TreeNode(value)
        else:
            self._insert_recursively(self.root_node, value)

    def _insert_recursively(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursively(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursively(node.right, value)

    def search(self, value):
        return self._search_recursively(self.root_node, value)

    def _search_recursively(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursively(node.left, value)
        return self._search_recursively(node.right, value)


def array_binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1


import random
import timeit

# Create a sorted array
sorted_array = list(range(10000))

# Shuffle the array
random.shuffle(sorted_array)

# Create a Binary Search Tree and insert elements
bst_tree = BinarySearchTree()
for element in sorted_array:
    bst_tree.insert(element)

# Measure BST search performance
def bst_tree_search_performance():
    total_time = 0
    for element in sorted_array:
        start_time = timeit.default_timer()
        bst_tree.search(element)
        end_time = timeit.default_timer()
        total_time += end_time - start_time
    return total_time / len(sorted_array), total_time

avg_bst_tree_search_time, total_bst_tree_search_time = bst_tree_search_performance()
print("Average BST search time:", avg_bst_tree_search_time)
print("Total BST search time:", total_bst_tree_search_time)

# Measure binary search in array performance
def array_binary_search_performance():
    total_time = 0
    for element in sorted_array:
        start_time = timeit.default_timer()
        array_binary_search(sorted_array, element)
        end_time = timeit.default_timer()
        total_time += end_time - start_time
    return total_time / len(sorted_array), total_time

avg_array_binary_search_time, total_array_binary_search_time = array_binary_search_performance()
print("Average array binary search time:", avg_array_binary_search_time)
print("Total array binary search time:", total_array_binary_search_time)

'''
In terms of time complexity, binary search in arrays outperforms searching in a Binary
 Search Tree because of its O(log n) complexity. In contrast, searching in a Binary 
 Search Tree has a time complexity of O(n), particularly in the worst-case scenario 
 where the tree's height equals its number of elements, resulting in O(n) time complexity. 
 Consequently, binary search in arrays is faster due to its more efficient time complexity. 
 Additionally, arrays provide better memory locality, which enhances cache performance, 
 further boosting their speed compared to Binary Search Trees.
'''