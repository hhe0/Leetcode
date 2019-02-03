class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node(None)
        self.length = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index > self.length-1 or index < 0:
            return -1

        i = 0
        ptr = self.head.next
        while i < index:
            i += 1
            ptr = ptr.next

        return ptr.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        temp_node = Node(val)

        if not self.head.next:
            self.head.next = temp_node
        else:
            temp_node.next = self.head.next
            self.head.next = temp_node
        self.length += 1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        ptr = self.head
        while ptr.next:
            ptr = ptr.next

        ptr.next = Node(val)
        self.length += 1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if index == 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        elif index < 0 or index > self.length:
            return None
        else:
            i = 0
            ptr = self.head.next
            while i < index-1:
                i += 1
                ptr = ptr.next
            temp_node = Node(val)
            temp_node.next = ptr.next
            ptr.next = temp_node
            self.length += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if not self.head.next:
            return None

        if index < 0 or index > self.length - 1:
            return None

        if index == 0:
            self.head.next = self.head.next.next
            return None

        i = 0
        ptr = self.head.next
        while i < index-1:
            i += 1
            ptr = ptr.next

        if i == self.length - 1:
            ptr.next = None
        else:
            ptr.next = ptr.next.next
        self.length -= 1


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# Your MyLinkedList object will be instantiated and called as such:


linkedList = MyLinkedList()
linkedList.addAtHead(0)
linkedList.addAtIndex(1, 9)
linkedList.addAtIndex(1, 5)
linkedList.addAtTail(7)
linkedList.addAtHead(1)
linkedList.addAtIndex(5, 8)
linkedList.addAtIndex(5, 2)
linkedList.addAtIndex(3, 0)
linkedList.addAtTail(1)
linkedList.addAtTail(0)
linkedList.deleteAtIndex(6)


# print(linkedList.get(1))       # 返回2
# print(linkedList.get(0))           # 返回3

head = linkedList.head.next
while head:
    print(head.val)
    head = head.next
