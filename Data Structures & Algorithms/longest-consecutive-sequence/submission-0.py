class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st=set(nums)
        maxlength=0
        currlength=1
        for i in nums:
            j=i
            if i-1 not in st:
                currlength=1
                while j+1 in st:
                    currlength+=1
                    j+=1
            maxlength=max(maxlength,currlength)
            
        return maxlength
                