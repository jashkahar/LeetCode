class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = "".join(a + b for a, b in zip(word1, word2))
        return merged + word1[len(word2):] + word2[len(word1):]

        # i, j = 0,0 
        # res = []

        # while i<len(word1) and j<len(word2):
        #     res.append(word1[i])
        #     res.append(word2[j])
        #     i += 1
        #     j += 1
        # res.append(word1[i:])
        # res.append(word2[j:])
        # return "".join(res)
        