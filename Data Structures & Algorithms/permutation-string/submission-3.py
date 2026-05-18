class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        window = len(s1)
        if len(s2) < window:
            return False
        if (window == 1):
            return s1 in s2
    
        sorted_s1 = ''.join(sorted(s1))
        if window == len(s2):
            return ''.join(sorted(s2)) == sorted_s1
        for i in range(len(s2) - window):
            print(s2[i+1:i+window+1])
            if sorted_s1 in ''.join(sorted(s2[i+1: i+window+1])):
                return True
        return False