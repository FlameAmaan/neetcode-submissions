class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        res,sol=[],[]
        
        def dfs():
            if len(sol)==n:
                res.append(sol.copy())
                return
            for i in nums:
                if i not in sol:
                    sol.append(i)
                    dfs()
                    sol.pop()
        dfs()
        return res
