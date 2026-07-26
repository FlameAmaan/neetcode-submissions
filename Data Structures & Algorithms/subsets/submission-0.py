class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        subset=[]
        def dfs(i):
            if i>=len(nums):
                res.append(subset.copy()) #empty subset
                return 
            #choosing to keep nums[i]
            subset.append(nums[i])
            dfs(i+1)
            #choosing to not keep nums[i]
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res