class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count, maxf = {}, 0
        res = 0
        l = 0 
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])
            currlen = r - l + 1
            if (currlen) - maxf <= k:
                res = max(res, currlen)
            else:
                count[s[l]] = count.get(s[l]) - 1
                l += 1
        return res



        