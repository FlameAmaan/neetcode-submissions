class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        visited=set()
        maxSize=0
        def bfs(r,c):
            size=1
            q=deque()
            q.append((r,c))
            visited.add((r,c))
            while q:
                row,col=q.popleft()
                directions=[[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in directions:
                    if (row+dr) in range(rows) and (col+dc) in range(cols) and grid[row+dr][col+dc]==1 and (row+dr,col+dc) not in visited:
                        q.append((row+dr,col+dc))
                        visited.add((row+dr,col+dc))
                        size+=1
            return size

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    maxSize=max(bfs(i,j),maxSize)
        return maxSize