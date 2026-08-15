class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited=set()
        rows,cols=len(grid),len(grid[0])
        q=deque()
        time=0
        def rotFruit(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or grid[r][c]!=1 or (r,c) in visited:
                return
            q.append((r,c))
            grid[r][c]=2
            visited.add((r,c))
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    q.append((i,j))
                    visited.add((i,j))
        while q:
            for i in range(len(q)):
                r,c=q.popleft()
                rotFruit(r+1,c)
                rotFruit(r,c+1)
                rotFruit(r-1,c)
                rotFruit(r,c-1)
            time+=1
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    return -1
        return time-1 if time else 0