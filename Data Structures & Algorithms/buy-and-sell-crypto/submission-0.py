class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far = prices[0]
        max_profit = 0
        for i in prices:
            min_so_far = min(i, min_so_far)
            max_profit = max(max_profit, i-min_so_far)
        return max_profit