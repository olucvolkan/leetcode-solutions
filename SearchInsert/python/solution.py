# https://leetcode.com/problems/search-insert-position/
class Solution:
    def search_insert(self, nums, target):
        low, high = 0, len(nums)
        mid = low + (high - low) / 2
        while mid != low:
            if nums[int(mid)] == target:
                return mid
            elif nums[mid] < target:
                low = mid
            else:
                high = mid
            mid = low + (high - low) / 2
        return mid if target <= nums[mid] else mid + 1
      
