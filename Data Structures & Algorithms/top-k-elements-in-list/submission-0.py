from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dicty = Counter(nums)
        return [ item[0] for item in dicty.most_common(k)]
    
