#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n= len(nums)

        for i in range(n):
            if(nums[i]!=val):
                nums.append(nums[i])

        for i in range(n):
            nums.pop(0)

        return len(nums)
        
# @lc code=end

