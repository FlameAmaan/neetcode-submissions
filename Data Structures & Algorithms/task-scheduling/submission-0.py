class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=Counter(tasks)
        maxHeap=[-x for x in count.values()]
        heapq.heapify(maxHeap)
        time=0
        q=deque() #holds the remaining occurences of a task,remaining idle time for that process
        while maxHeap or q:
            time+=1
            if maxHeap:
                cnt=1+heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt,time+n])
            if q and time==q[0][1]:
                heapq.heappush(maxHeap,q.popleft()[0])
        return time

            
                