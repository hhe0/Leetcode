# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None

        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


root = TreeNode(0)
node1 = TreeNode(1)
node2 = TreeNode(2)
root.left = node1
root.right = node2
node3 = TreeNode(3)
node4 = TreeNode(4)
node1.left = node3
node2.right = node4

solution = Solution()
res = solution.invertTree(root)
print(res.right.right.val)
