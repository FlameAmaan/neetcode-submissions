class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr=[]
        res=[]
        for i,point in enumerate(points):
            dist=((point[0]**2)+(point[1]**2))**(0.5)
            arr.append([dist,i])
        minHeap=arr
        heapq.heapify(minHeap)
        for i in range(k):
            x=heapq.heappop(minHeap)
            res.append(points[x[1]])
        return res
        