#1)Implement Binary tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, current_node, data):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert_recursive(current_node.left, data)
        else:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert_recursive(current_node.right, data)

    def search(self, data):
        return self._search_recursive(self.root, data)

    def _search_recursive(self, current_node, data):
        if current_node is None or current_node.data == data:
            return current_node
        if data < current_node.data:
            return self._search_recursive(current_node.left, data)
        return self._search_recursive(current_node.right, data)


tree = BinaryTree()
tree.insert(8)
tree.insert(3)
tree.insert(10)
tree.insert(1)
tree.insert(6)
tree.insert(14)
tree.insert(4)
tree.insert(7)
tree.insert(13)

result = tree.search(6)
if result:
    print("Value found!")
else:
    print("Value not found!")
#2)Find height of a given tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, current_node, data):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert_recursive(current_node.left, data)
        else:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert_recursive(current_node.right, data)

    def height(self):
        return self._height_recursive(self.root)

    def _height_recursive(self, current_node):
        if current_node is None:
            return 0
        left_height = self._height_recursive(current_node.left)
        right_height = self._height_recursive(current_node.right)
        return max(left_height, right_height) + 1
tree = BinaryTree()
tree.insert(8)
tree.insert(3)
tree.insert(10)
tree.insert(1)
tree.insert(6)
tree.insert(14)
tree.insert(4)
tree.insert(7)
tree.insert(13)
tree_height = tree.height()
print("Height of the tree:", tree_height)

#3)Perform Pre-order, Post-order, In-order traversal
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, current_node, data):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert_recursive(current_node.left, data)
        else:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert_recursive(current_node.right, data)

    def preorder_traversal(self):
        self._preorder_recursive(self.root)

    def _preorder_recursive(self, current_node):
        if current_node is not None:
            print(current_node.data, end=" ")
            self._preorder_recursive(current_node.left)
            self._preorder_recursive(current_node.right)

    def postorder_traversal(self):
        self._postorder_recursive(self.root)

    def _postorder_recursive(self, current_node):
        if current_node is not None:
            self._postorder_recursive(current_node.left)
            self._postorder_recursive(current_node.right)
            print(current_node.data, end=" ")

    def inorder_traversal(self):
        self._inorder_recursive(self.root)

    def _inorder_recursive(self, current_node):
        if current_node is not None:
            self._inorder_recursive(current_node.left)
            print(current_node.data, end=" ")
            self._inorder_recursive(current_node.right)
tree = BinaryTree()
tree.insert(8)
tree.insert(3)
tree.insert(10)
tree.insert(1)
tree.insert(6)
tree.insert(14)
tree.insert(4)
tree.insert(7)
tree.insert(13)
print("Pre-order traversal:")
tree.preorder_traversal()
print()
print("Post-order traversal:")
tree.postorder_traversal()
print()
print("In-order traversal:")
tree.inorder_traversal()
print()

#4)Function to print all the leaves in a given binary tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, current_node, data):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert_recursive(current_node.left, data)
        else:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert_recursive(current_node.right, data)

    def print_leaves(self):
        self._print_leaves_recursive(self.root)

    def _print_leaves_recursive(self, current_node):
        if current_node is not None:
            if current_node.left is None and current_node.right is None:
                print(current_node.data, end=" ")
            self._print_leaves_recursive(current_node.left)
            self._print_leaves_recursive(current_node.right)
tree = BinaryTree()
tree.insert(8)
tree.insert(3)
tree.insert(10)
tree.insert(1)
tree.insert(6)
tree.insert(14)
tree.insert(4)
tree.insert(7)
tree.insert(13)
print("Leaves of the tree:")
tree.print_leaves()
print()

#5)Implement BFS (Breath First Search) and DFS (Depth First Search)
from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, current_node, data):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert_recursive(current_node.left, data)
        else:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert_recursive(current_node.right, data)

    def breadth_first_search(self):
        if self.root is None:
            return
        queue = deque()
        queue.append(self.root)
        while queue:
            current_node = queue.popleft()
            print(current_node.data, end=" ")
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

    def depth_first_search(self):
        self._depth_first_search_recursive(self.root)

    def _depth_first_search_recursive(self, current_node):
        if current_node is not None:
            print(current_node.data, end=" ")
            self._depth_first_search_recursive(current_node.left)
            self._depth_first_search_recursive(current_node.right)
tree = BinaryTree()
tree.insert(8)
tree.insert(3)
tree.insert(10)
tree.insert(1)
tree.insert(6)
tree.insert(14)
tree.insert(4)
tree.insert(7)
tree.insert(13)
print("Breadth-First Search:")
tree.breadth_first_search()
print()
print("Depth-First Search:")
tree.depth_first_search()
print()

#6)Find sum of all left leaves in a given Binary Tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, current_node, data):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert_recursive(current_node.left, data)
        else:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert_recursive(current_node.right, data)

    def sum_left_leaves(self):
        return self._sum_left_leaves_recursive(self.root, False)

    def _sum_left_leaves_recursive(self, current_node, is_left):
        if current_node is None:
            return 0
        if current_node.left is None and current_node.right is None and is_left:
            return current_node.data
        left_sum = self._sum_left_leaves_recursive(current_node.left, True)
        right_sum = self._sum_left_leaves_recursive(current_node.right, False)
        return left_sum + right_sum
tree = BinaryTree()
tree.insert(8)
tree.insert(3)
tree.insert(10)
tree.insert(1)
tree.insert(6)
tree.insert(14)
tree.insert(4)
tree.insert(7)
tree.insert(13)
left_leaves_sum = tree.sum_left_leaves()
print("Sum of all left leaves:", left_leaves_sum)


#7)Find sum of all nodes of the given perfect binary tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def create_perfect_binary_tree(self, arr, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        node = Node(arr[mid])
        node.left = self.create_perfect_binary_tree(arr, start, mid - 1)
        node.right = self.create_perfect_binary_tree(arr, mid + 1, end)
        return node

    def sum_of_nodes(self):
        return self._sum_of_nodes_recursive(self.root)

    def _sum_of_nodes_recursive(self, current_node):
        if current_node is None:
            return 0
        return (
            current_node.data
            + self._sum_of_nodes_recursive(current_node.left)
            + self._sum_of_nodes_recursive(current_node.right)
        )
tree = BinaryTree()
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]  
tree.root = tree.create_perfect_binary_tree(arr, 0, len(arr) - 1)
sum_of_nodes = tree.sum_of_nodes()
print("Sum of all nodes:", sum_of_nodes)


#8)Count subtress that sum up to a given value x in a binary tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, current_node, data):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert_recursive(current_node.left, data)
        else:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert_recursive(current_node.right, data)

    def count_subtrees_with_sum(self, x):
        return self._count_subtrees_with_sum_recursive(self.root, x)[0]

    def _count_subtrees_with_sum_recursive(self, current_node, x):
        if current_node is None:
            return 0, 0

        left_count, left_sum = self._count_subtrees_with_sum_recursive(
            current_node.left, x
        )
        right_count, right_sum = self._count_subtrees_with_sum_recursive(
            current_node.right, x
        )

        total_count = left_count + right_count
        current_sum = current_node.data + left_sum + right_sum

        if current_sum == x:
            total_count += 1

        return total_count, current_sum
tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(2)
tree.insert(4)
tree.insert(8)
tree.insert(7)
tree.insert(9)
count = tree.count_subtrees_with_sum(7)
print("Number of subtrees with sum 7:", count)


#9)Find maximum level sum in Binary Tree
from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, current_node, data):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert_recursive(current_node.left, data)
        else:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert_recursive(current_node.right, data)

    def max_level_sum(self):
        if self.root is None:
            return 0

        queue = deque()
        queue.append(self.root)
        max_sum = float("-inf")
        while queue:
            level_sum = 0
            level_size = len(queue)
            for _ in range(level_size):
                current_node = queue.popleft()
                level_sum += current_node.data
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            max_sum = max(max_sum, level_sum)
        return max_sum
tree = BinaryTree()
tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)
tree.insert(6)
tree.insert(7)
max_sum = tree.max_level_sum()
print("Maximum level sum:", max_sum)

#10)Print the nodes at odd levels of a tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, current_node, data):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert_recursive(current_node.left, data)
        else:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert_recursive(current_node.right, data)

    def print_nodes_at_odd_levels(self):
        self._print_nodes_at_odd_levels_recursive(self.root, 1)

    def _print_nodes_at_odd_levels_recursive(self, current_node, level):
        if current_node is None:
            return

        if level % 2 == 1:
            print(current_node.data)

        self._print_nodes_at_odd_levels_recursive(current_node.left, level + 1)
        self._print_nodes_at_odd_levels_recursive(current_node.right, level + 1)
tree = BinaryTree()
tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)
tree.insert(6)
tree.insert(7)
print("Nodes at odd levels:")
tree.print_nodes_at_odd_levels()
