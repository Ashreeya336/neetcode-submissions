class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        list2 = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                list2[j] *= nums[i]
        return list2
