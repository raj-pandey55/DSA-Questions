#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        a=-1
        b=-1
        start = 0
        end = len(nums)-1
        while(start<=end):
            mid = start + (end-start)//2
            if((mid == 0 or nums[mid-1]<target) and nums[mid] == target):
                a = mid
                break
            elif(target > nums[mid]):
                
                start = mid + 1
            else:
                end = mid - 1
                

            
        start = 0
        end = len(nums)-1
    
        while(start<=end):
            mid = start + (end-start)//2
            if((mid == len(nums)-1 or nums[mid+1]>target) and nums[mid] == target):
                b = mid
                break
            elif(target < nums[mid]):
                
                end = mid - 1
            else:
                start = mid + 1
                

        return [a,b]                

        
# @lc code=end

