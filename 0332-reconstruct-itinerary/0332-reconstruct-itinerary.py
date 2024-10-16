class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        
        # Sort tickets in reverse order and construct the adjacency list
        tickets.sort(reverse=True)
        for src, dst in tickets:
            adj[src].append(dst)
        
        res = ["JFK"]

        def dfs(src):
            while adj[src]:
                # Always pick the last element because we've sorted in reverse order
                next_dest = adj[src].pop()
                dfs(next_dest)
            res.append(src)
        
        # Start DFS from JFK
        dfs("JFK")
        
        # The result list is constructed in reverse order, so we need to reverse it
        
        res = res[::-1]

        res.pop()
        return res