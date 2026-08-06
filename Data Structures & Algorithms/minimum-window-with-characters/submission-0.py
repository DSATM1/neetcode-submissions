from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        
        target_counts = Counter(t)
        required = len(target_counts)  

        window_counts = {}
        formed = 0  

        
        ans = (float("inf"), None, None)

        l = 0
        for r, char in enumerate(s):
            
            window_counts[char] = window_counts.get(char, 0) + 1

            if char in target_counts and window_counts[char] == target_counts[char]:
                formed += 1

            
            while l <= r and formed == required:
                
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                
                left_char = s[l]
                window_counts[left_char] -= 1
                if left_char in target_counts and window_counts[left_char] < target_counts[left_char]:
                    formed -= 1

                l += 1

        return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]