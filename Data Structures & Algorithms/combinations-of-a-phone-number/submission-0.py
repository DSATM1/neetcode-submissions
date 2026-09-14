class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
            
        digitToChar = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        res = []

        def backtrack(i, curStr):
            # Base condition: if the current string is the same length as the input digits
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            
            # Recursive step: iterate through characters mapped to the current digit
            for c in digitToChar[digits[i]]:
                backtrack(i + 1, curStr + c)
                
        backtrack(0, "")
        return res