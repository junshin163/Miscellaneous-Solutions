# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from functools import lru_cache
class Solution(object):
    @lru_cache(None)
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root.left == None or root.right == None:
            if root.left == None and root.right != None:
                if (root.right.val > root.val and self.smallestNode(root.right) > root.val 
                    and self.isValidBST(root.right) ):
                    return True
                return False
            if root.left != None and root.right == None:
                if (root.left.val < root.val and self.largestNode(root.left) < root.val 
                   and self.isValidBST(root.left) ):
                    return True
                return False
            else:
                return True
        if root.left.val < root.val and root.val < root.right.val:
            leftLargest = self.largestNode(root.left)
            rightSmallest = self.smallestNode(root.right)
            if (leftLargest < root.val and rightSmallest > root.val):
                if (self.isValidBST(root.left) and self.isValidBST(root.right) ):
                    return True
        return False
    
    def smallestNode(self, node):    # O(n)
        while node.left != None:
            node = node.left
        return node.val
    
    def largestNode(self, node):    # O(n)
        while node.right != None:
            node = node.right
        return node.val
