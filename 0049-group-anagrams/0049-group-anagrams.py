class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        
        for word in strs:
            key = tuple(sorted(word))
            anagrams[key].append(word)
        return list(anagrams.values()) 


        # res = defaultdict(list)
        
        # for s in strs:
        #     count = [0] * 26
        #     for c in s:
        #         count[ord(c) - ord("a")] += 1
        #     res[tuple(count)].append(s)
        #     # print(res)
        # return res.values()
        