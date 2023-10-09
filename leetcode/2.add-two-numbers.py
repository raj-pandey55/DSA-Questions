#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1=''
        temp=l1
        while(temp is not None):
            s1+= str(temp.val)
            temp=temp.next
        
        s2=''
        temp=l2
        while(temp is not None):
            s2+= str(temp.val)
            temp=temp.next
        
        s1=s1[::-1]
        s2=s2[::-1]
        print(s1,s2)
        # s1 = [str(i) for i in l]
        res1 = int("".join(s1))


        # s = [str(i) for i in m]
        res2 = int("".join(s2))

        res = res1 + res2
        res=str(res)
        # res = (str(res))[::-1]
        print(res)

        print(res)

        start = None
        for i in res:
            new = ListNode(i)
            new.next = None
            if(start == None):
                start = new
            else:
                new.next = start
                start = new

        return start
        
# @lc code=end

