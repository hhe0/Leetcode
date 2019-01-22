# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.res = []

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        res += self.inorderTraversal(root.left)
        res.append(root.val)
        res += self.inorderTraversal(root.right)

        return res


root = TreeNode(1)
leftRoot = TreeNode(2)
rightRoot = TreeNode(3)
root.left = leftRoot
root.right = rightRoot
solution = Solution()
print(solution.inorderTraversal(root))

