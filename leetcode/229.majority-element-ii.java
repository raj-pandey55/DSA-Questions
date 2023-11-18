
// # @lc app=leetcode id=229 lang=python
// #
// # [229] Majority Element II
// #
// # https://leetcode.com/problems/majority-element-ii/description/
// #
// # algorithms
// # Medium (46.97%)
// # Likes:    9139
// # Dislikes: 394
// # Total Accepted:    592.4K
// # Total Submissions: 1.2M
// # Testcase Example:  '[3,2,3]'
// #
// # Given an integer array of size n, find all elements that appear more than ⌊
// # n/3 ⌋ times.
// # 
// # 
// # Example 1:
// # 
// # 
// # Input: nums = [3,2,3]
// # Output: [3]
// # 
// # 
// # Example 2:
// # 
// # 
// # Input: nums = [1]
// # Output: [1]
// # 
// # 
// # Example 3:
// # 
// # 
// # Input: nums = [1,2]
// # Output: [1,2]
// # 
// # 
// # 
// # Constraints:
// # 
// # 
// # 1 <= nums.length <= 5 * 10^4
// # -10^9 <= nums[i] <= 10^9
// # 
// # 
// # 
// # Follow up: Could you solve the problem in linear time and in O(1) space?
//  
// 

//  @lc code=start
import java.util.*;
class Solution {
    public List<Integer> majorityElement(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int n = nums.length;
        
        for(int i=0;i<nums.length;i++){
            if(map.containsKey(nums[i])){
                map.put(nums[i],map.get(nums[i])+1);
            }
            else{
                map.put(nums[i],1);
            }
        }
        
        ArrayList<Integer> ans = new ArrayList<>();
        
        for(int key: map.keySet()){
            if(map.get(key)>n/3){
                ans.add(key);
            }
        }
        
        return ans;
    }
}
        
// @lc code=end

