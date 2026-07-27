class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        cur=[]
        def dfs(i,cur,total):
            if total==target:
                res.append(cur.copy())
                return 
            if total>target or i>=len(candidates):
                return
            
            #choosing nums[i]
            cur.append(candidates[i])
            dfs(i+1,cur,total+candidates[i])

            cur.pop()
            #choosing to skip
            while (i+1)<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            dfs(i+1,cur,total)
        dfs(0,cur,0)
        return res