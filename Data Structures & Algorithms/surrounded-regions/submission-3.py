class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS,COLS=len(board),len(board[0])
        def capture(r,c):
            if r not in range(ROWS) or c not in range(COLS) or board[r][c]!='O':
                return
            board[r][c]='T'
            capture(r+1,c)
            capture(r,c+1)
            capture(r-1,c)
            capture(r,c-1)
        for r in range(ROWS):
            for c in range(COLS):
                if r==0 or r==ROWS-1 or c==0 or c==COLS-1:
                    capture(r,c)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c]=='O':
                    board[r][c]='X'
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c]=='T':
                    board[r][c]='O'


