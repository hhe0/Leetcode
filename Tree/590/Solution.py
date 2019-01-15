# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        if not root.children:
            return [root.val]

        res = []
        for child in root.children:
            res += self.postorder(child)
        res += [root.val]

        return res


node1 = Node(1, None)
node2 = Node(3, None)
node3 = Node(2, None)
root = Node(0, [node1, node3, node2])

solution = Solution()
print(solution.postorder(root))

