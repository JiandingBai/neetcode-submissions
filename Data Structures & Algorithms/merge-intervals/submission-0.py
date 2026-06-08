class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda interval:interval[0])

        res = []
        
        for interval in intervals:
            if not res:
                res.append(interval)
            else:
                end = res[-1][1] 
                if end >= interval[0]:
                    res[-1][1] = max(end, interval[1])
                else:
                    res.append(interval)
        return res
        