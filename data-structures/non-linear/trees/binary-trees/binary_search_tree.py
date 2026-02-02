from collections import deque

class BinarySearchTree:
    """PUBLIC API"""
    class Node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right

    def __init__(self, rootval):
        self.root = self.Node(rootval)
        self._size = 1

    def insert(self, data):
        return self._insert(self.root, data)

    def contains(self, target):
        return self._contains(self.root, target)

    def preorder(self):
        return self._preorder(self.root)

    def inorder(self):
        return self._inorder(self.root)

    def postorder(self):
        return self._postorder(self.root)

    def levelorder(self):
        return self._levelorder(self.root)

    def __len__(self):
        return self._size


    """PRIVATE METHODS"""
    def _insert(self, root, data):
        """Insert a specific value in the Binary Search Tree"""
        if data <= root.data:
            if root.left is None:
                root.left = self.Node(data)
                self._size += 1
                return root.left
            self._insert(root.left, data)
        else:
            if root.right is None:
                root.right = self.Node(data)
                self._size += 1
                return root.right
            self._insert(root.right, data)


    def _contains(self, root, target):
        """Search for a target value in the Binary Search Tree"""
        if root is None:
            return False
        if target == root.data:
            return True
        if target < root.data:
            return self._contains(root.left, target)
        else:
            return self._contains(root.right, target)


    def _preorder(self, node):
        """Pre-order traversing. node.data -> left.data -> right.data"""
        if node is None:
            return
        print(node.data)
        self._preorder(node.left)
        self._preorder(node.right)


    def _inorder(self, node):
        """In-order traversing. left.data -> node.data -> right.data"""
        if node is None:
            return
        self._inorder(node.left)
        print(node.data)
        self._inorder(node.right)


    def _postorder(self, node):
        """Post-order traversing. left.data -> right.data -> node.data"""
        if node is None:
            return
        self._postorder(node.left)
        self._postorder(node.right)
        print(node.data)


    def _levelorder(self, root):
        """Breadth First Search traversal"""
        if root is None:
            return
        q = deque([root])
        while q:
            node = q.popleft()
            print(node.data)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)


tree = BinarySearchTree(10)
tree.insert(5)
tree.insert(15)
tree.insert(8)
tree.insert(3)
tree.insert(7)
