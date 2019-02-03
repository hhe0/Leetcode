# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 and not t2:
            return None
        elif not t1 and t2:
            return t2
        elif not t2 and t1:
            return t1
        else:
            node = TreeNode(t1.val + t2.val)
            node.left = self.mergeTrees(t1.left, t2.left)
            node.right = self.mergeTrees(t1.right, t2.right)

        return node


root1 = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(3)
root1.left = node1
root1.right = node2

root2 = TreeNode(1)
node3 = TreeNode(2)
node4 = TreeNode(3)
root2.left = node3
root2.right = node4

solution = Solution()
res = solution.mergeTrees(root1, root2)
print(res.left.val)
