class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap=[-x for x in stones]
        heapq.heapify(maxHeap)
        while(True):
            if len(maxHeap)==1:
                return -1*maxHeap[0]
            if len(maxHeap)==0:
                    return 0
            stone1=-1*(heapq.heappop(maxHeap))
            stone2=-1*(heapq.heappop(maxHeap))
            
            if stone1==stone2:
                continue
            if stone1<stone2:
                remaining=stone2-stone1
            else:
                remaining=stone1-stone2
            heapq.heappush(maxHeap,-1*remaining)