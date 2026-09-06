class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2==1:
            return False
        dp=set()
        dp.add(0)
        target=sum(nums)//2

        for i in range(len(nums)-1,-1,-1):
            nextDp=set()
            for j in dp:
                nextDp.add(j+nums[i])
                nextDp.add(j)
            dp=nextDp
        return True if target in dp else False
