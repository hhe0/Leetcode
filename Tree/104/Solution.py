# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


root = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(3)
root.left = node1
root.right = node2
solution = Solution()
print(solution.maxDepth(root))

