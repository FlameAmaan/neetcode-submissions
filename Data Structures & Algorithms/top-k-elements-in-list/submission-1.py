class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        res=[]
        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        sortedDict=sorted(count.items(),key=lambda x: x[1],reverse=True)
        for i in range(k):
            
            res.append(sortedDict[i][0])
            if len(res)==k:
                return res

            
        