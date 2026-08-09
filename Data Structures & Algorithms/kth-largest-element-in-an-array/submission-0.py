class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap=[-x for x in nums]
        heapq.heapify(minHeap)
        for i in range(k-1):
            heapq.heappop(minHeap)
        return -minHeap[0]