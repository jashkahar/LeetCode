class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        def dfs(city):
            visited.add(city)
            for sister in range(len(isConnected)):
                if isConnected[city][sister] and sister not in visited:
                    dfs(sister)
                
            
        provinces = 0
        visited =set()
        for city in range(len(isConnected)):
            if city not in visited:
                provinces += 1
                dfs(city)
        
        return provinces
         
            
        