class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product, zero_cnt = 1, 0
        for n in nums:
            if n:
                product *= n
            else:
                zero_cnt += 1
        
        result = [0] * len(nums)
        if zero_cnt > 1: return result
        
        for i, c in enumerate(nums):
            if zero_cnt: result[i] = 0 if c else product
            else: result[i] = product // c
        return result
        