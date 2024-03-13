class Solution:
    def pivotInteger(self, n: int) -> int:
        return int([x:=sqrt((1+n)*n//2),-1][x%1>0])