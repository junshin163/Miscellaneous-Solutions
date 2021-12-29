# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def helper(head):
            if(head == None):
                return None
            if(head.next == None):
                return head
            if(head.next.next == None):
                nxt = head.next
                nxt.next = head
                head.next = None
                return nxt
            #swap:
            nxt = head.next
            nxtnxt = head.next.next
            nxt.next = head
            head.next = helper(nxtnxt)
            return nxt
        return helper(head)
