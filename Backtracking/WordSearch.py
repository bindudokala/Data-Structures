class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        def backtrack(r, c, ind):
            if r < 0 or c < 0 or r == len(board) or c == len(board[r]) or board[r][c] != word[ind] or (r, c) in visited:
                return False
            visited.add((r, c))
            ind = ind + 1
            if ind == len(word):
                return True
            if backtrack(r, c + 1, ind):
                return True
            if backtrack(r, c - 1, ind):
                return True
            if backtrack(r - 1, c, ind):
                return True
            if backtrack(r + 1, c, ind):
                return True
            visited.remove((r, c))
            return False    

        for r in range(len(board)):
            for c in range(len(board[r])):
                if backtrack(r,c,0):
                    return True
        return False
        
        

'''📌 Main Idea:

The solution uses recursive backtracking with a visited set to explore possible paths starting from each cell in the grid.

* At each step, check if the current cell matches the expected character in the word.
* Mark the cell as visited to prevent revisiting it in the current path.
* Recursively explore all four possible directions: up, down, left, and right.
* If the complete word is formed (i.e., the index reaches the length of the given word), return `True`.
* If no valid path is found from the current cell, backtrack by unmarking the cell as visited and continue searching.
* If any starting point leads to a successful path, the function returns `True`; otherwise, it returns `False` after checking all possibilities.

📌 Time and Space Complexity:

* Time Complexity: `O(N * 3^L)`

  * `N` = total number of cells in the board.
  * `L` = length of the word.
  * Each cell explores up to 3 directions (not 4 because it won’t revisit the previous cell).

* Space Complexity: `O(L)`

  * For the recursion call stack and the `visited` set, which at most holds `L` cells (one for each character in the word).

Notes: I initially solved by passing another parameter called wordFormed to backtrack to store the word formed till now. 
But I realized it is not necessary since we already have ind which keeps the index of the given words as we reach end of the word, it implies the formed word is equal to the given word.
'''
