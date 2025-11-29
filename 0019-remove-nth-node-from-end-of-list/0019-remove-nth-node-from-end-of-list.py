# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head
        count = 0
        while fast and count < n:
            count += 1
            fast = fast.next
        if fast is None:
            return slow.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head
        
        
        # Solution 2 - first counting the total number of nodes and then moving to m - n index for nth node from last
        # temp = head
        # count = 0
        # while temp:
        #     count += 1
        #     temp = temp.next
        
        # temp1 = head
        # req = 0
        # prev = None
        # while req != (count - n):
        #     req += 1
        #     prev = temp1
        #     temp1 = temp1.next
        # if prev and temp1:
        #     prev.next = temp1.next
        # return head
        