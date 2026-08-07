class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        seen = set()
        def go(wi: int, r, c):
            if wi >= len(word):
                return True
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return False
            if (r, c) in seen:
                return False
            seen.add((r, c))
            if word[wi] != board[r][c]:
                return False 
            return (go(wi + 1, r + 1, c) or
                go(wi + 1, r - 1, c) or
                go(wi + 1, r, c + 1) or
                go(wi + 1, r, c - 1)
            )

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == word[0]:
                    seen = set()
                    if go(0, i, j):
                        return True
        return False

        
