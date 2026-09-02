class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<3:
                return max(nums)
        def robSpec(num):
            
            num[1]=max(num[1],num[0])
            for i in range(2,len(num)):
                num[i]=max(num[i]+num[i-2],num[i-1])
            return num[-1]
        return max(robSpec(nums[:-1]),robSpec(nums[1:]))