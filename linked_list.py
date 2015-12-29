#1.Given 1->2->3->3->4->5->3, val = 3, you should return the list as 1->2->4->5
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param val, an integer
    # @return a ListNode
    def removeElements(self, head, val):
        # Write your code here
        dummy = ListNode(0)
        dummy.next = head
        pre,cur = dummy,head
        
        while cur:
            if cur.val==val:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next
        return dummy.next
