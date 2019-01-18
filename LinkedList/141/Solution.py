# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        list = []
        while head:
            if id(head) in list:
                return True
            else:
                list.append(id(head))
                head = head.next

        return False


head = ListNode(2)
node1 = ListNode(6)
node2 = ListNode(3)

head.next = node1
node1.next = node2
# node2.next = node1

solution = Solution()
print(solution.hasCycle(head))
