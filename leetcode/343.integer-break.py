#
# @lc app=leetcode id=343 lang=python3
#
# [343] Integer Break
#

# @lc code=start
class Solution:
    def recur(self, n: int) -> int:
        if n<=4:
            return n
        else:
            return 3*self.recur(n-3)
    def integerBreak(self, n: int) -> int:
        

        if n<=3:
            return n-1
        elif n==4:
            return 4
        else:
            return self.recur(n)

# @lc code=end

