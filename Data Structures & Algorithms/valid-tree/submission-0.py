class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        map={i:[] for i in range(n)}
        visit=set()
        res=set()
        for edge in edges:
            map[edge[0]].append(edge[1])
            map[edge[1]].append(edge[0])
        def dfs(cur,parent):
            if cur in visit:
                return False
            visit.add(cur)
            res.add(cur)
            for i in map[cur]:
                if i!=parent:
                    if not dfs(i,cur):
                        return False
            visit.remove(cur)
            return True
        if n==0:
            return True
        if not dfs(0,None):
            return False
        return len(res)==n
        
        