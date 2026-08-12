
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        seen = set()
        ROWS, COLS = len(board), len(board[0])
        def go(r: int, c: int, i: int):
            if i >= len(word):
                return True
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return False
            if (r, c) in seen:
                return False
            if board[r][c] != word[i]:
                return False
            seen.add((r, c))
            result  = (
                go(r + 1, c, i + 1) or
                go(r, c + 1, i + 1) or
                go(r - 1, c, i + 1) or
                go(r, c - 1, i + 1)
            )
            seen.remove((r, c))
            return result
        

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if go(r, c, 0):
                        return True
        return False

