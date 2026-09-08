class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            current = nums[i]
            needed = target - current
            if needed in nums and nums.index(needed) != i:
                return sorted([i, nums.index(needed)])