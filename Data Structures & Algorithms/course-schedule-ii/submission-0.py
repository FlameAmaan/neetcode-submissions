class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap={i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        visit=set()
        res=[]
        def dfs(crs):
            if crs in visit:
                return False
            if preMap[crs]==[]:
                if crs not in res:
                    res.append(crs)
                return True
            visit.add(crs)
            for i in preMap[crs]:
                if not dfs(i): return False
            visit.remove(crs)
            preMap[crs]=[]
            if crs not in res:
                res.append(crs)
            return True
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res
