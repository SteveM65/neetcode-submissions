class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #Keep list of seen numbers
        #Check if is already in set -> Dups (False)
        #1. Rows
        for row in range(9):
            seen = set()
            for i in range(9):
                if board[row][i] == ".": 
                    continue
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i])

        #2. Columns
        for col in range(9):
            seen = set()
            for i in range(9):
                if board[i][col] == ".": 
                    continue
                if board[i][col] in seen:
                    return False
                seen.add(board[i][col])

        #3. 3x3 sub-boxes 
        
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square%3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])

        return True

        