class Solution:
    def trap(self, height: List[int]) -> int:
        water_store = [0]
        for i in range(1, len(height)-1):
            left = max(height[i], max(height[i:]))
            right = max(height[i] , max(height[:i]))
            water_store.append(min(left, right) - height[i])
        return sum(water_store)