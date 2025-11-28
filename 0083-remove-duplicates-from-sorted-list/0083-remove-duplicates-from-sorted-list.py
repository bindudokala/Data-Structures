# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp, start = head, head
        while temp!= None and start != None:
            while temp.next and temp.val == temp.next.val:
                temp = temp.next
            start.next = temp.next
            start = temp.next
            temp = temp.next
        return head
