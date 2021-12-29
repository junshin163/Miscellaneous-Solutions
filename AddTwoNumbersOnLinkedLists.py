# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        first_summand = 0
        first_exponent = 0
        second_summand = 0
        second_exponent = 0
        while l1 != None:
            first_summand += (10 ** first_exponent) * l1.val
            first_exponent += 1
            if l1.next != None:
                l1 = l1.next
            else:
                l1 = None
        while l2 != None:
            second_summand += (10 ** second_exponent) * l2.val
            second_exponent += 1
            if l2.next != None:
                l2 = l2.next
            else:
                l2 = None
        result = first_summand + second_summand
        
        
        first_digit = result % 10
        first_node = ListNode(first_digit)
        current_node = first_node
        result /= 10
        while result > 0:
            digit = result % 10
            new_node = ListNode(digit)
            current_node.next = new_node
            current_node = new_node
            result /= 10
        return first_node
