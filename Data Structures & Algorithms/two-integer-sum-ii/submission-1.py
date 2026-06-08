class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        myMap = {}
        for i, n in enumerate(numbers):
            need = target - n
            if need in myMap:
                return [myMap[need] + 1, i + 1] 
            myMap[n] = i
        return []


        