class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, pal = [], []
        def backtrack(ind):
            if ind == len(s):
                res.append(pal[:])
                return
            for i in range(ind, len(s)):
                if self.isPalindrome(s[ind: i + 1]):
                    pal.append(s[ind : i + 1])
                    backtrack(i + 1)
                    pal.pop()
                
        backtrack(0)
        return res

    def isPalindrome(self, s1):
        l, r = 0, len(s1) - 1
        while l <= r:
            if s1[l] != s1[r]:
                return False
            l += 1
            r -= 1
        return True
        


'''
Start: "aab"
├── "a" (palindrome)
│   ├── "a" (palindrome)
│   │   └── "b" (palindrome) → ["a","a","b"]
│   └── "ab" (not palindrome ❌)
└── "aa" (palindrome)
    └── "b" (palindrome) → ["aa","b"]

    
📌 Main Idea of Your Code:
Use backtracking to explore all possible ways to partition the string such that every substring is a palindrome.

At every recursive call:

• ind represents the starting index from which we will explore substrings.

• The loop iterates from ind to the end of the string, checking substrings s[ind:i+1]

• If a substring s[ind:i+1] is a palindrome:

    • Add it to pal (current partition path)

    • Then recursively call backtrack(i+1) to explore further partitions starting from i+1

    • Once that path is fully explored, you backtrack by popping the last element.


Notes:
• At any point, if we are at index i inside the loop, it means we are considering the substring from ind to i (inclusive) to decide whether to add it to the current partition or not.

• ind is the start of the next substring we're trying to partition.

• i moves from ind to len(s)-1, picking end points for substrings starting at ind.


⏳ Time :   O(n * 2^n)
🗂️ Space :  O(n * 2^n)
'''