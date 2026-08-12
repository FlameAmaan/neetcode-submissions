class MedianFinder:

    def __init__(self):
        self.leftHeap=[]
        self.rightHeap=[]
        heapq.heapify(self.leftHeap)
        heapq.heapify(self.rightHeap)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.leftHeap,-1*num)
        if (self.leftHeap and self.rightHeap) and -1*self.leftHeap[0]>self.rightHeap[0]:
            heapq.heappush(self.rightHeap,-1*heapq.heappop(self.leftHeap))
        if len(self.leftHeap)>len(self.rightHeap)+1:
            heapq.heappush(self.rightHeap,-1*heapq.heappop(self.leftHeap))
        elif len(self.rightHeap)>len(self.leftHeap)+1:
            heapq.heappush(self.leftHeap,-1*heapq.heappop(self.rightHeap))

    def findMedian(self) -> float:
        if (len(self.leftHeap)+len(self.rightHeap))%2==0:
            return ((-1*self.leftHeap[0])+self.rightHeap[0])/2
        elif len(self.leftHeap)>len(self.rightHeap):
            return -1*self.leftHeap[0]
        else:
            return self.rightHeap[0]
        

        