class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # anagrams = defaultdict(list)
        
        # for char in strs:
        #     # print(sorted(set(char)))
            
        #     anagrams["".join(sorted(set(char)))].append(char)
        # print(sorted(anagrams.values()))
        # return anagrams       
        res = defaultdict(list)
        
        for s in strs:
            count = [0] * 26
            
            for c in s:
                count[ord(c) - ord("a")] += 1
            
            
            res[tuple(count)].append(s)
        return res.values()
        