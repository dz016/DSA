# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        prev=None
        Next = None

        while current:
            Next = current.next
            current.next = prev
            prev = current
            current = Next

        return prev
