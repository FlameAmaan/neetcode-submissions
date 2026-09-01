class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        map={i:[] for i in range(n)}
        visit=set()
        component=0
        for edge in edges:
            map[edge[0]].append(edge[1])
            map[edge[1]].append(edge[0])
        def dfs(node,parent):
            if node in visit:
                return
            visit.add(node)
            for i in map[node]:
                if i!=parent:
                    dfs(i,node)
        for i in range(n):
            if i not in visit:
                component+=1
                dfs(i,None)
        return component

