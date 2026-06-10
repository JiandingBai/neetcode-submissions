class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        while len(stones) > 1:
            stones.sort(reverse = True)

            y = stones[0]
            x = stones[1]

            if x == y:
                stones = stones[2:len(stones)]
            elif x < y:
                stones.pop(1)
                stones[0] = y - x
        
        if not stones:
            return 0
        else:
            return stones[0]

        