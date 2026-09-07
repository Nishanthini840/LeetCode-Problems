class Solution(object):
    def deleteNode(self, root, key):
        if root is None:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:
            if root.left is None:
                return root.right

            if root.right is None:
                return root.left

            current = root.right

            while current.left:
                current = current.left

            root.val = current.val
            root.right = self.deleteNode(root.right, current.val)

        return root
        