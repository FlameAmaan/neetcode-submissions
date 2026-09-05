class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxdp=[float("-inf")]*len(nums)
        mindp=[float("inf")]*len(nums)
        maxdp[0]=nums[0]
        mindp[0]=nums[0]
        for i in range(1,len(nums)):
            maxdp[i]=max(nums[i],nums[i]*maxdp[i-1],nums[i]*mindp[i-1])
            mindp[i]=min(nums[i],nums[i]*maxdp[i-1],nums[i]*mindp[i-1])
        return max(maxdp)