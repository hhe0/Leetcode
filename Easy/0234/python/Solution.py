# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        link_list = []
        while head:
            link_list.append(head.val)
            head = head.next

        start = 0
        end = len(link_list) - 1
        while start <= end:
            if link_list[start] != link_list[end]:
                return False
            else:
                start += 1
                end -= 1

        return True


head = ListNode(1)
node1 = ListNode(2)
head.next = node1
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(1)
node2.next = node3
# node4 = ListNode(2)
# node3.next = node4

solution = Solution()
print(solution.isPalindrome(head))
