class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        obtainable = 0
        added = 0
        coins.sort()

        for coin in coins:
            while coin > obtainable + 1:
                added += 1
                newCoin = obtainable + 1
                obtainable += newCoin
                if obtainable >= target:
                    return added
            obtainable += coin
            if obtainable >= target:
                return added
        while obtainable < target:
            added += 1
            newCoin = obtainable + 1
            obtainable += newCoin
        return added
