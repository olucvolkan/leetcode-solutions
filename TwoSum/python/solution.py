# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            second_value = nums.index(target - nums[i])
            if second_value:
                return [i, second_value]
            else:
                return

              
