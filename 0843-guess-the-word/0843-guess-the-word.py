# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        def removeInvalidWord():
            filteredList = []
            for w in words:
                if pair_match(guess_word, w) == match:
                    filteredList.append(w)
            return filteredList

        def pair_match(a,b):
            return sum(c1==c2 for c1, c2 in zip(a,b))
        
        def getMostCoomonWord():
            counts = [[0]*26 for _ in range(6)]

            for w in words:
                for i,c in enumerate(w):
                    counts[i][ord(c)-ord('a')] += 1
            
            best_score = 0
            best_word = ""

            for w in words:
                curScore = 0
                for i,c in enumerate(w):
                    curScore += counts[i][ord(c)-ord('a')]

                if curScore > best_score:
                    best_score = curScore
                    best_word = w
            return best_word


        while words:
            guess_word = getMostCoomonWord()

            match = master.guess(guess_word)

            if match == 6:
                return
            
            words = removeInvalidWord() 
