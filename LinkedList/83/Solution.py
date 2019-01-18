# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        link_list = []
        while head:
            if head.val not in link_list:
                link_list.append(head.val)
            head = head.next

        if not link_list:
            return None

        res = ListNode(link_list[0])
        head = res

        for i in range(1, len(link_list)):
            temp = ListNode(link_list[i])
            head.next = temp
            head = temp

        return res


head = ListNode(0)
node1 = ListNode(1)
head.next = node1
node2 = ListNode(1)
node1.next = node2
node3 = ListNode(0)
node2.next = node3
node4 = ListNode(2)
node3.next = node4

solution = Solution()
res = solution.deleteDuplicates(head)
while res:
    print(res.val)
    res = res.next
