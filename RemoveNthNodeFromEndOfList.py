# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        #first compute the total length:
        node = head
        list_length = 0
        while node != None:
            list_length += 1
            node = node.next
        
        
        if list_length == 0:
            return None
        if list_length == 1:
            return None
        if list_length == 2:
            if n == 1:
                head.next = None
                return head
            else:
                return head.next
        
        #Below is O(N) for any list of length > 2
        #delete the (list_length - n+1)th node:
        #edge case where we delete first item:
        if n == list_length:
            return head.next
        
        node_before_del = head
        for i in range(1, list_length - n):
            node_before_del = node_before_del.next
        node_to_del = node_before_del.next
        node_after_del = node_to_del.next
        node_to_del.next = None
        node_before_del.next = node_after_del
        return head
