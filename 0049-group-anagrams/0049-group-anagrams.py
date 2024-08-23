class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        
        for word in strs:
            # Sort the characters of the word to create a key
            key = tuple(sorted(word))
            anagrams[key].append(word)
        
        return list(anagrams.values())      
        # res = defaultdict(list)
        
        # for s in strs:
        #     count = [0] * 26
            
        #     for c in s:
        #         count[ord(c) - ord("a")] += 1
        #     res[tuple(count)].append(s)
        # print(count)
        # return res.values()
        