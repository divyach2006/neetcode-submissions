class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      for i in range(len(nums)):
         no1=nums[i]
         no2=target-no1
         if no2 in nums and nums.index(no2) != i:
           return sorted([i,nums.index(no2)])