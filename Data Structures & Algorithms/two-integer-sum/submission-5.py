class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictu = {}
        for i in range(0, len(nums)): 
            if (target - nums[i]) in dictu:
                return [dictu[target-nums[i]], i]
            else: 
                dictu[nums[i]] = i