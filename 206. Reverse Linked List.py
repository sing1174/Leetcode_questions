"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

 
Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:

Input: head = [1,2]
Output: [2,1]

Example 3:

Input: head = []
Output: []
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # initialize current and prev 
        curr = head
        prev = None

        while curr is not None:
            # store next node value
            nextNode = curr.next

            # reverse current node pointer direction
            curr.next = prev

            # update prev and current nodes
            prev = curr
            curr = nextNode

        return prev
        
