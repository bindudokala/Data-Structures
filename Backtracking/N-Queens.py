class Solution:
    def isSafe(self, r, c, board):
        row = r - 1
        while(row >= 0):
            if board[row][c] == "Q":
                return False
            row -= 1
        
        row, col = r - 1, c - 1
        while(row >= 0 and col >= 0):
            if board[row][col] == "Q":
                return False
            row -= 1
            col -= 1

        row, col = r - 1, c + 1
        while(row >= 0 and col < len(board)):
            if board[row][col] == "Q":
                return False
            row -= 1
            col += 1
        return True

    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."]*n for x in range(n)]
        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return            
            for c in range(n):
                if self.isSafe(r, c, board):
                    board[r][c] = "Q"
                    backtrack(r + 1)
                    board[r][c] = "."
        backtrack(0)
        return res
            


'''
📌 Main Idea of the N-Queens Problem:
The goal is to place N queens on an N*N chessboard such that:

No two queens attack each other.

Queens can move any number of squares vertically, horizontally, or diagonally.


📖 How It Works:

At each step:

• Check each column in the current row r.

• Use isSafe to see if placing a queen at position (r, c) would lead to a conflict with already-placed queens.

    • Check vertically upward.

    • Check diagonally upward to the left.

    • Check diagonally upward to the right.

• If it's safe:

    • Place a queen ("Q").

    • Recurse to the next row.

    • After recursion (whether it succeeded or failed), backtrack by removing the queen (reset to ".") — this is crucial to explore all configurations.

• If you reach the base case r == n, it means a valid configuration is formed — convert the board to a list of strings and add it to the results.


⏳ Time :   O(n * n!)
🗂️ Space :  O(n^2)
'''



# Solution 2 - backtracking using hashsets
def solveNQueens(self, n: int) -> List[List[str]]:
    res = []
    board = [["."]*n for x in range(n)]
    colQueens, leftDiagonal, rightDiagonal = set(), set(), set()
    def backtrack(r):
        if r == n:
            copy = ["".join(row) for row in board]
            res.append(copy)
            return
        for c in range(n):
            if c in colQueens or (r-c) in leftDiagonal or (r+c) in rightDiagonal:
                continue
            board[r][c] = "Q"
            colQueens.add(c)
            leftDiagonal.add(r-c)
            rightDiagonal.add(r+c)

            backtrack(r + 1)

            board[r][c] = "."
            colQueens.remove(c)
            leftDiagonal.remove(r-c)
            rightDiagonal.remove(r+c)
    backtrack(0)
    return res



'''
For Solution 2 - Use a Hashset to store the queens placed in each row, column, left diagonal and right diagonal:
At any time:

• colQueens → contains the set of columns where a queen is already placed.

• leftDiagonal → contains the set of left diagonals (r - c) already occupied.

•rightDiagonal → contains the set of right diagonals (r + c) already occupied.

📌 Why r-c and r+c?
• In a matrix, cells on the same left diagonal have the same value of r - c.

• Cells on the same right diagonal have the same value of r + c.

⏳ Time :   O(n!)
🗂️ Space :  O(n^2)
'''