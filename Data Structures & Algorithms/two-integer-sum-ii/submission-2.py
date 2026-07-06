class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i,j=0,len(numbers)-1
        res=[]
        while i<j:
            if numbers[i]+numbers[j]>target:
                j-=1
            elif numbers[i]+numbers[j]<target:
                i+=1
            elif numbers[i]+numbers[j]==target:
                res.append(i+1)
                res.append(j+1)
                return res
        return res