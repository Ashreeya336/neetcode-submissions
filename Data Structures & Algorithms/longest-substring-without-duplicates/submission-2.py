class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if (len(s)<2):
            return len(s)
        sub_s = s[1]
        max_window = 1
        j = 0
        while j <len(s):
            if s[j] in sub_s:
                sub_s = sub_s[sub_s.find(s[j])+1:]+s[j]
            else:
                sub_s = sub_s + s[j]
            max_window = max(max_window, len(sub_s))
            j = j+1
        return max_window

    



