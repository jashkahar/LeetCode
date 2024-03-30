class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        c = 0
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            return True
        for i in range(len(flowerbed) - 1):
            # print(i)
            if c == n:
                return True
            if i == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                # print('in first if')
                flowerbed[i] = 1
                c += 1
            if (
                i != 0
                and flowerbed[i] == 0
                and flowerbed[i + 1] == 0
                and flowerbed[i - 1] == 0
            ):
                # print('in second if')
                # print(i)
                flowerbed[i] = 1
                c += 1
            if i == len(flowerbed) and flowerbed[i] == 0 and flowerbed[i - 1] == 0:
                # print('in thir if')
                flowerbed[i] = 1
                c += 1
        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            # print('in fourth if')
            flowerbed[-1] = 1
            c += 1
        if c == n:
            return True
        else:
            return False
