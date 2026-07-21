# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left=right=head
        prev=None
        for i in range(n):
            right=right.next
        if not right:
            return head.next
        while right:
            prev=left
            left=left.next
            right=right.next
        prev.next=left.next
        left.next=None
        return head
            

