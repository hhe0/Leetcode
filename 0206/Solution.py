# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_head = ListNode(0)
        ptr = head
        while ptr:
            if new_head.next:
                temp = ptr
                ptr = ptr.next
                temp.next = new_head.next
                new_head.next = temp
            else:
                new_head.next = ptr
                ptr = ptr.next
                # 不要忘记这一步置空操作
                new_head.next.next = None

        return new_head.next


node = ListNode(1)
n1 = ListNode(1)
node.next = n1
n2 = ListNode(2)
n1.next = n2
n3 = ListNode(3)
n2.next = n3
n4 = ListNode(4)
n3.next = n4
n5 = ListNode(5)
n4.next = n5

solution = Solution()
head1 = solution.reverseList(node)

while head1:
    print(head1.val)
    head1 = head1.next

