class Solution:
    def encode(self, strs: list[str]) -> str:
        res = ""
        for s in strs:
            # Append the length of the string, a delimiter, and the string itself
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> list[str]:
        res, i = [], 0
        
        while i < len(s):
            j = i
            # Move j forward until we find the delimiter to extract the length
            while s[j] != "#":
                j += 1
            
            # Extract the integer length of the string
            length = int(s[i:j])
            
            # Extract the actual string using the length
            # j + 1 is where the string starts
            res.append(s[j + 1 : j + 1 + length])
            
            # Move the i pointer to the start of the next encoded string
            i = j + 1 + length
            
        return res