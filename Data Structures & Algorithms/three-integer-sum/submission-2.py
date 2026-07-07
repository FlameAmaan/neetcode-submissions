class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        for i,val in enumerate(nums):
            if i>0 and val==nums[i-1]:
                continue
            j=i+1
            k=len(nums)-1
            while(j<k):
                if nums[j]+nums[k]>-1*(nums[i]):
                    k-=1
                elif nums[j]+nums[k]<-1*(nums[i]):
                    j+=1
                else:
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    while nums[j]==nums[j-1] and j<k:
                        j+=1
        return res



        