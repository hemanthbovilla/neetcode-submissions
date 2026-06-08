class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_sorted = sorted(s1)   # keep sorted version of s1
        n = len(s1)

        # only substrings of length n matter
        for i in range(len(s2) - n + 1):
            subStr = s2[i:i+n]   # take substring of length n
            if sorted(subStr) == s1_sorted:
                return True
        return False
