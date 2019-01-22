# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        if not root.children:
            return 1
        return max(self.maxDepth(x) for x in root.children) + 1


node1 = Node(1, None)
node2 = Node(2, None)
node3 = Node(3, None)
root = Node(1, [node1, node2, node3])

solution = Solution()
print(solution.maxDepth(root))

