class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(open_count, close_count, current_string):
            # If the string is fully formed (length 2 * n), add it to results
            if open_count == close_count == n:
                res.append(current_string)
                return

            # We can always add an open parenthesis if we haven't reached n
            if open_count < n:
                backtrack(open_count + 1, close_count, current_string + "(")

            # We can only add a close parenthesis if there are unmatched open parentheses
            if close_count < open_count:
                backtrack(open_count, close_count + 1, current_string + ")")

        backtrack(0, 0, "")
        return res