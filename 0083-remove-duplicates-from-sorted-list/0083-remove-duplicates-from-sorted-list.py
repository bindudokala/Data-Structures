# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Solution - 1
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head

        # Solution 2 - start and end pointers to keep track of the start and end of duplicates
        # start, end = head, head
        # while start!= None and end != None:
        #     while end.next and end.val == end.next.val:
        #         end = end.next
        #     start.next = end.next
        #     start = end.next
        #     end = end.next
        # return head
