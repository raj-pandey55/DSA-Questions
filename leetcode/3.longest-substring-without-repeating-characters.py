#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=[]
        count=0
        b=[]
        for i in range(len(s)):
            if s[i] in l:
                l=l[l.index(s[i])+1:]
                # l=l[0+l.index(s[i]):]
            l.append(s[i])
            count=len(l)
            b.append(count)

        if(s==''):
            return 0
        return max(b)
        
# @lc code=end

