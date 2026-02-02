from collections import deque

class BinaryTree:
    """PUBLIC API"""
    class Node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right

    def __init__(self, rootval):
        self.root = self.Node(rootval)
        self._size = 1

    def preorder(self):
        return self._preorder(self.root)

    def inorder(self):
        return self._inorder(self.root)

    def postorder(self):
        return self._postorder(self.root)

    def levelorder(self):
        return self._levelorder(self.root)

    def insert(self, data):
        return self._insert(self.root, data)

    def __len__(self):
        return self._size


    """PRIVATE METHODS"""
    def _insert(self, root, data):
        """Insert a specific value in the Binary Tree"""
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
        """Breadth First Search in the Binary Tree"""
        if root is None:
            return
        q = deque([root])
        while q:
            node = q.popleft()
            print(node.data)
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)


tree = BinaryTree(56)
tree.insert(52)
tree.insert(14)
tree.insert(-5)
tree.insert(56)
tree.insert(19)
tree.insert(90)
