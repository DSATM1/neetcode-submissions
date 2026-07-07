class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = s.lower().replace(" ", "")
        t = t.lower().replace(" ", "")
        return sorted(s) == sorted(t)