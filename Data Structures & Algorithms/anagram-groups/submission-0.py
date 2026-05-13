class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictu = {}
        for i in strs:
            sortu = "".join(sorted(i))
            if sortu in dictu:
                dictu[sortu].append(i)
            else:
                dictu[sortu] = [i]
        
        return list(dictu.values())