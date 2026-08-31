class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class MyLinkedList:
    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, index: int) -> int:
        if index < self.size:
            if index <= self.size // 2:
                curr = self.head

                for i in range(index + 1):
                    curr = curr.next

                return curr.val

            else:
                curr = self.tail

                for i in range(self.size - index):
                    curr = curr.prev

                return curr.val

        else:
            return -1

    def getPrev(self, index: int) -> ListNode:
        if index <= self.size // 2:
            curr = self.head

            for i in range(index):
                curr = curr.next

            return curr

        else:
            curr = self.tail

            for i in range(self.size - index + 1):
                curr = curr.prev

            return curr

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        else:
            prev = self.getPrev(index)
            next_node = prev.next

            node = ListNode(val)

            node.prev = prev
            node.next = next_node

            next_node.prev = node
            prev.next = node

            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return 
        else:
            prev = self.getPrev(index)
            curr = prev.next

            prev.next = curr.next
            curr.next.prev = prev

            self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
