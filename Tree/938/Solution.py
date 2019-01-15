# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if not root:
            return 0
        if root.val < L:
            return self.rangeSumBST(root.right, L, R)
        elif root.val > R:
            return self.rangeSumBST(root.left, L, R)
        else:
            return root.val + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)


root = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(3)
node3 = TreeNode(4)
node4 = TreeNode(5)
root.left = node1
root.right = node2
node1.left = node3
node1.right = node4
solution = Solution()
print(solution.rangeSumBST(root, 1, 3))
