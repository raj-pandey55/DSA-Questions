#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#
# https://leetcode.com/problems/combination-sum-ii/description/
#
# algorithms
# Medium (53.74%)
# Likes:    9690
# Dislikes: 247
# Total Accepted:    835.4K
# Total Submissions: 1.6M
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# Given a collection of candidate numbers (candidates) and a target number
# (target), find all unique combinations in candidates where the candidate
# numbers sum to target.
# 
# Each number in candidates may only be used once in the combination.
# 
# Note: The solution set must not contain duplicate combinations.
# 
# 
# Example 1:
# 
# 
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# 
# 
# Example 2:
# 
# 
# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30
# 
# 
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        candidates.sort()
        n=len(candidates)
        def comb(arr,ind,n,temp,ans,target):
            
            if(target==0):

                ans.append(temp.copy())
                    
                return
            
            for i in range(ind,n):
                if(i>ind and arr[i]==arr[i-1]):
                    continue
                elif(arr[i]>target):
                    break
                
            
            
                temp.append(arr[i])
                comb(arr,i+1,n,temp,ans,target-arr[i])
                temp.pop()

        comb(candidates,0,n,[],ans,target)

        
        
        
        return ans
# @lc code=end

