# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1:
            return list2
        elif not list2:
            return list1

        output, curr1, curr2 = ListNode(), list1, list2
        dummy = output

        while curr1 and curr2:

            if curr1.val <= curr2.val:
                dummy.next = curr1
                curr1 = curr1.next
            else:
                dummy.next = curr2
                curr2 = curr2.next

            dummy = dummy.next

        if curr1 is None and curr2:
            dummy.next = curr2
        else:
            dummy.next = curr1

        return output.next
                
                