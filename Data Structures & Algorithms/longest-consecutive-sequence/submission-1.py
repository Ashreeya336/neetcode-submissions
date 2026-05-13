class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        max_seq = 1;
        curr_seq = 1;
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                curr_seq += 1
            elif nums[i] == nums[i-1]:
                continue
            else:
                curr_seq = 1
            if curr_seq > max_seq:
                max_seq = curr_seq
        if curr_seq > max_seq:
                return curr_seq
        return max_seq