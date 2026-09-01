class ListNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def queue(self, tail):
        self.prev = tail.prev
        self.prev.next = self
        self.next = tail
        tail.prev = self

    def dequeue(self):
        self.prev.next = self.next
        self.next.prev = self.prev


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        head = ListNode(0)
        tail = ListNode(0)

        head.next = tail
        tail.prev = head

        result = len(students)

        for student in students:
            node = ListNode(student)
            node.queue(tail)

        counter = 0

        while sandwiches and counter < result:
            curr = head.next
            if curr.val == sandwiches[0]:
                curr.dequeue()
                result -= 1
                sandwiches.pop(0)
                counter = 0
            else:
                curr.dequeue()
                curr.queue(tail)
                counter += 1

        return result

        
