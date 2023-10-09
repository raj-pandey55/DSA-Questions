#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#
# https://leetcode.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (63.09%)
# Likes:    11282
# Dislikes: 409
# Total Accepted:    1.2M
# Total Submissions: 1.9M
# Testcase Example:  '[1,2,3,4]'
#
# Given a linked list, swap every two adjacent nodes and return its head. You
# must solve the problem without modifying the values in the list's nodes
# (i.e., only nodes themselves may be changed.)
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]
# 
# 
# Example 2:
# 
# 
# Input: head = []
# Output: []
# 
# 
# Example 3:
# 
# 
# Input: head = [1]
# Output: [1]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is in the range [0, 100].
# 0 <= Node.val <= 100
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        if(temp is None):
            return head
        if(temp.next is None):
            return head

        while(temp is not None):
            if(temp.next is None):
                return head
            l=[]
            l.append(temp.val)
            l.append(temp.next.val)
            x,y=l[0],l[1]
            temp.val=y
            temp.next.val=x
            print(head)
            
            temp=temp.next.next

        return head

        
# @lc code=end

