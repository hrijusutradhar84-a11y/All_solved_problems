"""
Binary Search Tree (BST)

Problem: Implement a Binary Search Tree with basic operations: insert, search, and inorder traversal.

Time Complexity: O(log n) average, O(n) worst case
Space Complexity: O(n)

Example:
    >>> bst = BST()
    >>> bst.insert(50).insert(30).insert(70).insert(20).insert(40)
    >>> bst.search(40)
    True
    >>> bst.inorder()
    [20, 30, 40, 50, 70]
"""

class Node:
    """
    A node in the binary search tree.
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    """
    Binary Search Tree implementation.
    """
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        """
        Insert a value into the BST.
        
        Args:
            value: Value to insert
        
        Returns:
            self for method chaining
        """
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_helper(self.root, value)
        return self
    
    def _insert_helper(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_helper(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_helper(node.right, value)
    
    def search(self, value):
        """
        Search for a value in the BST.
        
        Args:
            value: Value to search
        
        Returns:
            bool: True if found, False otherwise
        """
        return self._search_helper(self.root, value)
    
    def _search_helper(self, node, value):
        if node is None:
            return False
        
        if value == node.value:
            return True
        elif value < node.value:
            return self._search_helper(node.left, value)
        else:
            return self._search_helper(node.right, value)
    
    def inorder(self):
        """
        Inorder traversal of the BST.
        
        Returns:
            list: Inorder traversal result
        """
        result = []
        self._inorder_helper(self.root, result)
        return result
    
    def _inorder_helper(self, node, result):
        if node is None:
            return
        
        self._inorder_helper(node.left, result)
        result.append(node.value)
        self._inorder_helper(node.right, result)
    
    def preorder(self):
        """
        Preorder traversal of the BST.
        
        Returns:
            list: Preorder traversal result
        """
        result = []
        self._preorder_helper(self.root, result)
        return result
    
    def _preorder_helper(self, node, result):
        if node is None:
            return
        
        result.append(node.value)
        self._preorder_helper(node.left, result)
        self._preorder_helper(node.right, result)


if __name__ == "__main__":
    bst = BST()
    bst.insert(50).insert(30).insert(70).insert(20).insert(40).insert(60).insert(80)
    
    print("Test 1 (inorder):", bst.inorder())      # [20, 30, 40, 50, 60, 70, 80]
    print("Test 2 (preorder):", bst.preorder())    # [50, 30, 20, 40, 70, 60, 80]
    print("Test 3 (search 40):", bst.search(40))   # True
    print("Test 4 (search 100):", bst.search(100)) # False
