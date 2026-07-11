class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start,end=1,max(piles)
        
        while start<=end:
            mid=(start+end)//2
            total=0
            for j in piles:
                total+=math.ceil(j/mid)
            if total<=h:
                end=mid-1
                res=mid
            else:
                start=mid+1
        return res
            

                
            
        

