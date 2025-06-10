class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitsToLetters = {"2":"abc",
                           "3":"def",
                           "4":"ghi",
                           "5":"jkl",
                           "6":"mno",
                           "7":"pqrs",
                           "8":"tuv",
                           "9":"wxyz"
                           }
        def backtrack(ind, currComb):
            if ind == len(digits):
                res.append(currComb)
                return
            for dig in digitsToLetters[digits[ind]]:
                backtrack(ind + 1, currComb + dig)
        if digits:
            backtrack(0, "")
        return res



'''
📌 Main Idea of the Code:
Use backtracking (recursive DFS) to explore all possible letter combinations that can be formed by mapping each digit to its corresponding letters (like on a phone keypad).

📖 How It Works:
• digitsToLetters: A dictionary mapping each digit ('2' to '9') to its possible letters.

• backtrack(ind, currComb):

    •ind is the current position in the digits string.

    •currComb is the combination formed so far.

• At every recursive call:

    • If ind equals the length of the input string digits:
     → A complete combination is formed → add it to res.

    • Else:

        • Loop over the possible letters for digits[ind].

        • For each letter:

            • Append it to currComb.

            • Move to the next digit by calling backtrack(ind+1, currComb+letter).

• Only call backtrack if digits is non-empty.


⏳ Time :   O(n * 4^n)
🗂️ Space :  O(n * 4^n)
'''