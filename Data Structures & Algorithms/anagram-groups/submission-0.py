class Solution:
    def sortString(self,s):
        s1 = list(s)
        s1.sort()
        return "".join(s1)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = {}
        for s in strs:
            key = self.sortString(s)
            if key in dct:
                dct[key].append(s)
            else:
                dct[key] = [s]

        return list(dct.values())