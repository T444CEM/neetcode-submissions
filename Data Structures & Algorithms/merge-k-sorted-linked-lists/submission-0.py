# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedList = []

            for i in range(0, len(lists), 2):

                list1 = lists[i]
                list2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedList.append(self.mergeList(list1, list2))
            lists = mergedList 

        return lists[0]

    def mergeList(self, left, right):
        dummy = ListNode()
        tail = dummy

        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next

            tail = tail.next
        
        if left:
            tail.next = left
        if right:
            tail.next = right
        
        return dummy.next




