# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        f = ListNode(0)
        if l1.val + l2. val > 9:
            f.val = l1.val + l2.val -10
            n = 1
        else:
            f.val = l1.val + l2.val
            n = 0
        i = f
        while l1.next != None or l2.next != None or n != 0:
            if l1.next == None:
                a = 0
            else:
                l1 = l1.next
                a = l1.val
                
            if l2.next == None:
                b = 0
            else:
                l2 = l2.next
                b = l2.val
            
            j = ListNode(0)
            if a + b + n > 9:
                j.val = a + b + n - 10
                n = 1
            else:
                j.val = a + b + n
                n = 0
            i.next = j
            i = i.next
        return f