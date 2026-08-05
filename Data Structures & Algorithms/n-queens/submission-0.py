class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col=set()   #holds queen with a specific column value
        posDiag=set() #holds a (r+c) value
        negDiag=set() #holds a (r-c) value
        res=[]
        board=[["."]*n for i in range(n)]
        def dfs(r):
            if r==n:
                copy=["".join(row) for row in board]
                res.append(copy)
                return 
            for c in range(n):
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue
                board[r][c]="Q"
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                dfs(r+1)
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c]="."
        dfs(0)
        return res
                    
        
