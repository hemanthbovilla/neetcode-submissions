class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        charset = set(s)
        
        for c in charset:
            l = 0
            count = 0
            for r in range(len(s)):
                if s[r] == c:
                    count += 1
                # shrink window if replacements exceed k
                while (r - l + 1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1
                # update result with current valid window size
                res = max(res, r - l + 1)
        
        return res
