#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        a=x
        a=abs(a)
        res=0
        while(a!=0):
            res = res*10+ a%10
            a=a//10

        

        if(x<0):
            res= -1*res
        else:
            res=  res

        if(res<pow(-2,31) or res>(pow(2,31)-1)):
            return 0
        else:
            return res

# @lc code=end

