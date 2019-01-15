# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if (root.left and root.left.val != root.val) or (root.right and root.right.val != root.val):
            return False

        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)


root1 = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(3)
# root1.left = node1
# root1.right = node2

solution = Solution()
print(solution.isUnivalTree(root1))
