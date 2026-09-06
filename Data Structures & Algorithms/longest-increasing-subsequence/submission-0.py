class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[1]*len(nums)
        dp[len(nums)-1]=1
        for i in range(len(nums)-2,-1,-1):
            for j in range(i+1,len(dp)):
                if nums[j]>nums[i]:
                    dp[i]=max(dp[i],1+dp[j])
                else:
                    dp[i]=max(dp[i],1)
            
        return max(dp)