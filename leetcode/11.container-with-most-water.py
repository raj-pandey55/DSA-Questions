#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        l=[]
        maximum = 0
        while(i<j):
            amount=(j-i)*min(height[i],height[j])
            maximum=max(amount,maximum)
            if(height[i]>height[j]):
                j-=1
            else:
                i+=1
    
            
        return maximum
        
# @lc code=end

