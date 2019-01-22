# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        val = max(nums)
        pos = nums.index(val)

        root = TreeNode(val)

        left = nums[:pos]
        if len(left):
            root.left = self.constructMaximumBinaryTree(left)

        right = nums[pos+1:]
        if len(right):
            root.right = self.constructMaximumBinaryTree(right)

        return root


solution = Solution()
res = solution.constructMaximumBinaryTree([1, 3, 2, 4, 2, 7, 3])
print(res.left.val)
